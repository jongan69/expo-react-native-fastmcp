import pytest
from pathlib import Path
import server

@pytest.fixture(scope="module", autouse=True)
def use_real_docs_dir():
    """Ensure the server uses the actual docs directory for all tests."""
    orig_docs_dir = server.docs_dir
    server.docs_dir = Path("docs")
    server.register_markdown_resources()
    yield
    server.docs_dir = orig_docs_dir

def test_search_docs():
    """Test that searching for 'react' returns at least one match and all results have snippets."""
    results = server.search_docs("react")
    print(f"search_docs('react') results: {results}")
    assert any(r["matches"] > 0 for r in results), "No matches found for 'react' in docs"
    assert all("snippet" in r for r in results), "Not all results have a 'snippet' field"

def test_fuzzy_search_docs():
    """Test that fuzzy search for a typo returns results with scores."""
    results = server.fuzzy_search_docs("typo-tolernt", threshold=60)
    print(f"fuzzy_search_docs('typo-tolernt') results: {results}")
    assert all("score" in r for r in results), "Not all fuzzy search results have a 'score' field"

def test_advanced_search_keyword():
    """Test that advanced search by keyword 'android' returns relevant results."""
    results = server.advanced_search(keyword="android")
    print(f"advanced_search(keyword='android') results: {results}")
    assert any("android" in r["snippet"].lower() or "android" in r["filename"].lower() for r in results), "No relevant results for keyword 'android'"

def test_advanced_search_tag():
    """Test that advanced search by tag 'guide' returns only results with that tag."""
    results = server.advanced_search(tag="guide")
    print(f"advanced_search(tag='guide') results: {results}")
    assert all("guide" in (r.get("tags") or []) for r in results), "Not all results have the 'guide' tag"

def test_advanced_search_after():
    """Test that advanced search after a very old date returns results."""
    results = server.advanced_search(after="2000-01-01T00:00:00")
    print(f"advanced_search(after='2000-01-01T00:00:00') results: {results}")
    assert len(results) > 0, "No results returned for advanced search after a very old date"

def test_get_doc_content():
    """Test that getting content for a real file returns text, and for a nonexistent file returns an empty string."""
    filename = "textinput"  # Example, adjust as needed
    content = server.get_doc_content(filename)
    print(f"get_doc_content('{filename}') content: {content[:100]}...")
    assert isinstance(content, str), "Content is not a string"
    assert len(content) > 0, f"No content returned for file '{filename}'"
    content = server.get_doc_content("nonexistent")
    print(f"get_doc_content('nonexistent') content: {content}")
    assert content == "", "Nonexistent file did not return an empty string" 