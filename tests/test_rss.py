"""
    Tests the gab driver.
"""
import re
import unittest
from typing import List

import feedparser
from bs4 import BeautifulSoup
from gabposter import gab_post

# from rss2gab import gab_driver

RSS_FEED = "http://Bigleaguepolitics.com/feed"

STRICT = False

USER = "testgabposter"
PASS = "Yq4F2H9Lvp"

POST_IMAGE = False

def _html_to_text(html):
    """
    Converts HTML to text.
    """
    try:
        soup = BeautifulSoup(html.replace(r"\n", "<br>"), "html.parser")
        return soup.get_text()
    except Exception as err:  # pylint: disable=broad-except
        if STRICT:
            raise
        print(f"{__file__}: Warning, bad characters in html: {err}")
        # Use a regular expression to remove all HTML tags
        return re.sub("<[^<]+?>", "", html)


def _find_all_img_urls(text: str) -> List[str]:
    """
    Returns the first image in the text.
    """
    img_url_pattern = r"https?://[^\s]+\.(?:png|jpg|jpeg|gif)"
    # Use a regular expression to find all image urls
    img_urls = re.findall(img_url_pattern, text)
    return img_urls


class RssTester(unittest.TestCase):
    """Gab driver test framework."""

    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        feed = feedparser.parse(RSS_FEED)
        for entry in feed.entries:
            title = entry.title
            link = entry.link
            # summary = entry.summary
            description = entry.description
            text = _html_to_text(description)
            imgs = _find_all_img_urls(description)
            print(f"title: {title}")
            print(f"text: {text}")
            print(f"imgs: {imgs}")
            img = imgs[0] if imgs and POST_IMAGE else None
            content = title + "\n\n" + link
            gab_post(username=USER, password=PASS, content=content, jpg_path=img, dry_run=True)


if __name__ == "__main__":
    unittest.main()
