import os
import json
import requests
from markdownify import markdownify
import time
import re
from urllib.parse import urlparse

def scrape_markdown():
    with open("sitemaps_urls.json") as f:
        all_urls = json.load(f)

    def safe_filename(url):
        # Use only the last segment of the URL path, excluding trailing slashes
        parsed = urlparse(url)
        path = parsed.path.rstrip('/')
        last_segment = path.split('/')[-1] or 'index'
        # Remove unsafe chars
        filename = re.sub(r'[^a-zA-Z0-9_-]', '_', last_segment)
        return filename[:100]  # limit length for safety

    os.makedirs("docs", exist_ok=True)

    for group, urls in all_urls.items():
        print(f"Processing group: {group}, {len(urls)} URLs")
        for url in urls:
            print(f"Fetching: {url}")
            try:
                resp = requests.get(url, timeout=15)
                if resp.status_code == 200:
                    md = markdownify(resp.text)
                    filename = safe_filename(url) + ".md"
                    filepath = os.path.join("docs", filename)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(md)
                else:
                    print(f"<error>Failed to fetch: {resp.status_code}</error>")
            except Exception as e:
                print(f"<error>{e}</error>")
            time.sleep(0.5)  # Be polite to the server

# Run the script
if __name__ == "__main__":
    scrape_markdown()
