"""
    Tests the gab driver.
"""
import unittest

from rss2gab import gab_driver

USER = "testgabposter"
PASS = "Yq4F2H9Lvp"


class GabDriverTest(unittest.TestCase):
    """Gab driver test framework."""

    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works"""
        gab_driver.gab_post(USER, PASS, "test", dry_run=True)

    @unittest.skip("Live testing disabled")
    def test_live_posting(self) -> None:
        """Tests that gab_post works"""
        gab_driver.gab_post(USER, PASS, "test", dry_run=False)


if __name__ == "__main__":
    unittest.main()
