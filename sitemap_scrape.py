import requests
from bs4 import BeautifulSoup
import json
# Requires: pip install lxml

# Define the sitemap URL
expo_sitemap_url = 'https://docs.expo.dev/sitemap.xml'
react_native_sitemap_url = 'https://reactnative.dev/sitemap.xml'

def scrape_sitemap(url):
    # Send a GET request to the sitemap URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the XML content using lxml
        soup = BeautifulSoup(response.text, 'lxml-xml')
        # Find all URLs in the sitemap
        urls = [loc.text for loc in soup.find_all('loc')]
        return urls
    else:
        print(f"Failed to fetch sitemap: {url}")
        return []

if __name__ == "__main__":
    expo_urls = scrape_sitemap(expo_sitemap_url)
    react_native_urls = scrape_sitemap(react_native_sitemap_url)
    all_urls = {
        "expo": expo_urls,
        "react_native": react_native_urls
    }
    with open("sitemaps_urls.json", "w") as f:
        json.dump(all_urls, f, indent=2)

