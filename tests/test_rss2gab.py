"""
    Tests parsing an rss feed.
"""
import unittest

from gabposter import gab_test
from rss2gab import rss2gab

RSS_FEED = "http://Bigleaguepolitics.com/feed"
GAB_LOGIN_USER = "testgabposter"
GAB_LOGIN_PASS = "Yq4F2H9Lvp"
GAB_ID = "testgabposter"  # Outward facing username, like gab.com/username


class RssTester(unittest.TestCase):
    """Gab driver test framework."""

    @unittest.skip("Not implemented yet")
    def test_gab_test(self) -> None:
        """Sanity test to make sure that the browser can connect to the web."""
        self.assertTrue(gab_test())

    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        rss2gab(
            RSS_FEED,
            GAB_ID,
            GAB_LOGIN_USER,
            GAB_LOGIN_PASS,
            dry_run=True,
            limit=1,
        )


if __name__ == "__main__":
    unittest.main()
