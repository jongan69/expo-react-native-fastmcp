from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.resources.types import FileResource
from pathlib import Path
import datetime
import yaml
from rapidfuzz import fuzz
import logging

mcp = FastMCP("React Native Expo Markdown Documentation Server")
docs_dir = Path("docs")

# Setup logging
logging.basicConfig(filename="mcp_server_queries.log", level=logging.INFO, format="%(asctime)s %(message)s")

def extract_tags_and_version(file: Path):
    tags = []
    version = None
    try:
        with open(file, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            if first_line == "---":
                lines = []
                for line in f:
                    if line.strip() == "---":
                        break
                    lines.append(line)
                meta = yaml.safe_load("".join(lines))
                tags = meta.get("tags", []) if meta else []
                version = str(meta.get("version")) if meta and "version" in meta else None
    except Exception:
        pass
    return tags, version

def get_file_metadata(file: Path):
    stat = file.stat()
    last_modified = datetime.datetime.fromtimestamp(stat.st_mtime).isoformat()
    return {"last_modified": last_modified}

def register_markdown_resources():
    if not docs_dir.exists():
        return
    for file in docs_dir.glob("*.md"):
        # Validate file is not empty and is readable
        try:
            if file.stat().st_size == 0:
                continue
            with open(file, "r", encoding="utf-8") as f:
                f.read()
        except Exception:
            continue
        tags, version = extract_tags_and_version(file)
        uri = f"docs://{file.stem}"
        metadata = get_file_metadata(file)
        description = f"Markdown documentation: {file.stem} (Last modified: {metadata['last_modified']})"
        if tags:
            description += f" [tags: {', '.join(tags)}]"
        if version:
            description += f" [version: {version}]"
        mcp.add_resource(
            FileResource(
                uri=uri,
                name=file.stem,
                description=description,
                path=file.resolve(),
                mime_type="text/markdown",
            )
        )

register_markdown_resources()

@mcp.tool(description="Search documentation for a keyword and return ranked filenames with context snippets.")
def search_docs(keyword: str) -> list[dict]:
    logging.info(f"search_docs: {keyword}")
    results = []
    keyword_lower = keyword.lower()
    for file in docs_dir.glob("*.md"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                content_lower = content.lower()
                if keyword_lower in content_lower:
                    count = content_lower.count(keyword_lower)
                    idx = content_lower.find(keyword_lower)
                    snippet = content[max(0, idx-30):idx+30] if idx != -1 else ""
                    tags, version = extract_tags_and_version(file)
                    results.append({
                        "filename": file.stem,
                        "matches": count,
                        "snippet": snippet.strip().replace('\n', ' '),
                        "last_modified": get_file_metadata(file)["last_modified"],
                        "tags": tags,
                        "version": version
                    })
        except Exception:
            continue
    results.sort(key=lambda x: x["matches"], reverse=True)
    return results

@mcp.tool(description="Fuzzy search documentation for a keyword (typo-tolerant) and return ranked results with context snippets.")
def fuzzy_search_docs(keyword: str, threshold: int = 70) -> list[dict]:
    logging.info(f"fuzzy_search_docs: {keyword}, threshold={threshold}")
    results = []
    for file in docs_dir.glob("*.md"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                score = fuzz.partial_ratio(keyword.lower(), content.lower())
                if score >= threshold:
                    tags, version = extract_tags_and_version(file)
                    results.append({
                        "filename": file.stem,
                        "score": score,
                        "snippet": content[:60].replace('\n', ' '),
                        "last_modified": get_file_metadata(file)["last_modified"],
                        "tags": tags,
                        "version": version
                    })
        except Exception:
            continue
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

@mcp.tool(description="Advanced search: by keyword, tag, or last modified date (ISO format). Returns ranked results.")
def advanced_search(keyword: str = "", tag: str = "", after: str = "") -> list[dict]:
    logging.info(f"advanced_search: keyword={keyword}, tag={tag}, after={after}")
    results = []
    keyword_lower = keyword.lower() if keyword else None
    for file in docs_dir.glob("*.md"):
        tags, version = extract_tags_and_version(file)
        meta = get_file_metadata(file)
        if tag and tag not in tags:
            continue
        if after and meta["last_modified"] < after:
            continue
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                content_lower = content.lower()
                if keyword_lower and keyword_lower not in content_lower:
                    continue
                count = content_lower.count(keyword_lower) if keyword_lower else 0
                idx = content_lower.find(keyword_lower) if keyword_lower else 0
                snippet = content[max(0, idx-30):idx+30] if keyword_lower and idx != -1 else content[:60]
                results.append({
                    "filename": file.stem,
                    "matches": count,
                    "snippet": snippet.strip().replace('\n', ' '),
                    "last_modified": meta["last_modified"],
                    "tags": tags,
                    "version": version
                })
        except Exception:
            continue
    results.sort(key=lambda x: x["matches"], reverse=True)
    return results

@mcp.tool(description="Get full content of a documentation file by name.")
def get_doc_content(filename: str) -> str:
    logging.info(f"get_doc_content: {filename}")
    file = docs_dir / f"{filename}.md"
    if file.exists():
        return file.read_text(encoding="utf-8")
    return ""

if __name__ == "__main__":
    mcp.run(transport="stdio")
    # mcp.run()