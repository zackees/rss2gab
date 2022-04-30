"""
    Tests parsing an rss feed.
"""
import unittest
from datetime import datetime, timedelta

from rss2gab.parse_rss_feed import parse_rss_feed

# from rss2gab import gab_driver

RSS_FEED = "http://Bigleaguepolitics.com/feed"

USER = "testgabposter"
PASS = "Yq4F2H9Lvp"

POST_IMAGE = False


class RssTester(unittest.TestCase):
    """Gab driver test framework."""

    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        now = datetime.now()
        max_age = timedelta(days=5)
        published_after = now - max_age
        rss_entries = parse_rss_feed(RSS_FEED, published_after=published_after)
        self.assertTrue(len(rss_entries) > 0)
        for entry in rss_entries:
            age = now - entry.published
            self.assertLessEqual(age, max_age)


if __name__ == "__main__":
    unittest.main()
