"""
    Tests parsing an rss feed.
"""
import unittest

from gabposter import gab_post
from rss2gab.parse_rss_feed import parse_rss_feed

# from rss2gab import gab_driver

RSS_FEED = "http://Bigleaguepolitics.com/feed"

USER = "testgabposter"
PASS = "Yq4F2H9Lvp"

POST_IMAGE = False


class RssTester(unittest.TestCase):
    """Gab driver test framework."""

    @unittest.skip("Live testing disabled")
    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        content_list = parse_rss_feed(RSS_FEED)
        for content, img in content_list:
            if not POST_IMAGE:
                img = None
            gab_post(USER, PASS, content=content, jpg_path=img, dry_run=True)


if __name__ == "__main__":
    unittest.main()
