"""Scraper module for fetching website content."""

import requests
from bs4 import BeautifulSoup


def fetch_website_content(url: str) -> str:
    """
    Fetch and extract main text content from a URL.

    Args:
        url: The webpage URL to fetch.

    Returns:
        Extracted text content from the page.

    Raises:
        requests.RequestException: On request or connection errors.
    """
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove script and style elements
    for tag in soup(["script", "style"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    # Collapse multiple whitespace
    return " ".join(text.split())
