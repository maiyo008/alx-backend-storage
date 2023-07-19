#!/usr/bin/env python3
"""
web.py
"""
import requests
import redis
import time
from typing import Optional


cache = redis.Redis()
CACHE_EXPIRATION_TIME = 10  # 10 seconds


def get_page(url: str) -> Optional[str]:
    """
    Obtain the HTML content of a particular URL and returns it
    """
    cached_html = cache.get(url)
    if cached_html:
        return cached_html.decode("utf-8")
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        cache.setex(url, CACHE_EXPIRATION_TIME, html_content)
        return html_content
    return None


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"  # Replace with your desired URL
    start_time = time.time()
    for _ in range(5):
        html_content = get_page(url)
        print(f"HTML content length: {len(html_content)}")
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
