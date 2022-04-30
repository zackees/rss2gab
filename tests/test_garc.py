"""
    Tests the gab driver.
"""

import unittest

from rss2gab.gab_readposts import gab_readposts

GAB_ACCOUNT_TO_FETCH = "bigleaguepol"
GAB_LOGIN_USER = "testgabposter"
GAB_LOGIN_PASS = "Yq4F2H9Lvp"


class GarcTester(unittest.TestCase):
    """Gab driver test framework."""

    def test_fetch_bigleague(self) -> None:
        """Tests that we can read bigleague politics from the test acccount."""
        posts = gab_readposts(
            gab_id=GAB_ACCOUNT_TO_FETCH,
            gab_login_user=GAB_LOGIN_USER,
            gab_login_pass=GAB_LOGIN_PASS,
        )
        self.assertTrue(len(posts) > 0)


if __name__ == "__main__":
    unittest.main()
