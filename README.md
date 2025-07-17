[![MseeP.ai Security Assessment Badge](https://mseep.net/two-tailed_swallowtail_s0jdo4.jpg)](https://mseep.ai/app/jongan69-expo-react-native-fastmcp)

# 📚 Expo React Native Markdown Documentation Server (MCP)

A fast, extensible, and intelligent documentation server for Markdown files using React Native Expo Documentation, powered by the MCP framework.

---

## 🚀 Features

- **Automatic Markdown Discovery:** Scans the `docs/` directory for all Markdown files and registers them as searchable resources.
- **Metadata Extraction:** Reads YAML frontmatter for tags and versioning, and tracks last modified dates.
- **Powerful Search Tools:**
  - **Keyword Search:** Find documentation by exact keyword matches, with ranked results and context snippets.
  - **Fuzzy Search:** Typo-tolerant search using rapidfuzz for partial matches.
  - **Advanced Search:** Filter by keyword, tag, and/or last modified date.
- **Resource API:** Exposes documentation as resources with rich metadata for integration with other tools.
- **Logging:** All queries are logged for analytics and debugging.
- **Simple API:** Exposes all search and retrieval tools via MCP's tool interface.

---

## 🏗️ Project Structure

```
.
├── server.py         # Main server code (this file)
├── docs/            # Place your Markdown documentation here
│   └── *.md
├── sitemap_scrape.py  # Scrapes Expo and React Native Sitemaps for Documentation URLS and saves to sitemaps_urls.json
├── scrape_markdown.py  # Scrapes sitemaps_urls.json URLs and saves the data as *.md files in /docs
└── README.md
```

---

## 🛠️ Usage

### 1. Add Your Documentation

Place your Markdown files in the `docs/` directory or use `sitemap_scrape.py` and `scrape_markdown.py` to generate *.md files from a sitemap url.  

Optionally, add YAML frontmatter for tags and versioning:

```markdown
---
tags: [api, quickstart]
version: 1.2.0
---

# My API Documentation

Welcome to the docs!
```

### 2. Start the Server

Note: use `source .venv/bin/activate` to activate the python enviornment 

```bash
 uv run mcp dev server.py 
```

The server runs using MCP's `stdio` transport by default.

---

## 🔍 API Overview

All tools are exposed via the MCP tool interface:

### `search_docs(keyword: str)`

- **Description:** Search for a keyword in all docs. Returns ranked filenames with context snippets.
- **Returns:**
  - `filename`
  - `matches` (count)
  - `snippet`
  - `last_modified`
  - `tags`
  - `version`

---

### `fuzzy_search_docs(keyword: str, threshold: int = 70)`

- **Description:** Typo-tolerant search using rapidfuzz. Returns ranked results with context.
- **Returns:**
  - `filename`
  - `score`
  - `snippet`
  - `last_modified`
  - `tags`
  - `version`

---

### `advanced_search(keyword: str = "", tag: str = "", after: str = "")`

- **Description:** Search by keyword, tag, or last modified date (ISO format).
- **Returns:**
  - `filename`
  - `matches`
  - `snippet`
  - `last_modified`
  - `tags`
  - `version`

---

### `get_doc_content(filename: str)`

- **Description:** Retrieve the full content of a documentation file by name.

---

## 📝 Example Query

```python
from mcp.client import MCPClient

client = MCPClient("http://localhost:YOUR_PORT")
results = client.search_docs("installation")
print(results)
```

---

## 🍾 Adding to Cursor

Use the `mcp.json` file structure for using the MCP server in Cursor 

## 🧩 Extending

- Add new Markdown files to `docs/` — they are auto-discovered.
- Add new search tools or resource types by extending `server.py`.

---

## 🛡️ Logging

All queries are logged to `mcp_server_queries.log` for traceability and analytics.

---

## 🧑‍💻 Requirements

- Python 3.8+
- [mcp](https://github.com/multiprocessio/mcp)
- [PyYAML](https://pyyaml.org/)
- [rapidfuzz](https://github.com/maxbachmann/RapidFuzz)

Install dependencies:

```bash
pip install mcp pyyaml rapidfuzz
```

---

## 🤝 Contributing

Pull requests and issues are welcome!  
Feel free to suggest features or improvements.

---

## 📄 License

MIT License

---

## ✨ Credits

Built with [MCP](https://github.com/multiprocessio/mcp) and ❤️ by yours truly.
