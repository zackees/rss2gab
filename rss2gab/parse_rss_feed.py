"""
    Tests the gab driver.
"""
import re
from typing import List, Optional

from dataclasses import dataclass

import feedparser  # type: ignore

_IMG_URL_PATTERN = r"https?://[^\s]+\.(?:png|jpg|jpeg|gif)"

@dataclass
class RssEntry:
    """Simple object of parsed RSS entries."""
    content: str = ""
    img: Optional[str] = None


def _find_all_img_urls(text: str) -> List[str]:
    """
    Returns all image urls in a string.
    """
    # Use a regular expression to find all image urls
    img_urls = re.findall(_IMG_URL_PATTERN, text)
    return img_urls


def _feed_entry_to_content(entry: feedparser.FeedParserDict) -> RssEntry:
    """
    Converts a feedparser entry to a content string.
    """
    title = entry.title
    link = entry.link
    description = entry.description
    imgs = _find_all_img_urls(description)
    img = imgs[0] if imgs else None
    content = title + "\n\n" + link
    return RssEntry(content, img)


def parse_rss_feed(feed_url: str, limit: int = 100) -> List[RssEntry]:
    """
    Generates gab posts from a feed.
    """
    feed = feedparser.parse(feed_url)
    entries = feed.entries[:limit]
    contents = []
    for entry in entries:
        rss_entry = _feed_entry_to_content(entry)
        contents.append(rss_entry)
    return contents
