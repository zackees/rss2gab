"""
    Tests the gab driver.
"""

import unittest
from pprint import pprint

from rss2gab.gab_readposts import gab_readposts

ACCOUNT = "bigleaguepol"


class GarcTester(unittest.TestCase):
    """Gab driver test framework."""

    def test_fetch_bigleague(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        posts = gab_readposts(user=ACCOUNT)
        pprint(posts)


if __name__ == "__main__":
    unittest.main()
