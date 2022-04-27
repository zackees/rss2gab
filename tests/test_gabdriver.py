"""
    Tests the gab driver.
"""
import os
import unittest

from rss2gab import gab_driver

HERE = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(HERE, "data")
SMALL_IMG = os.path.join(TEST_DATA, "small.jpg")


USER = "testgabposter"
PASS = "Yq4F2H9Lvp"


class GabDriverTest(unittest.TestCase):
    """Gab driver test framework."""

    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        gab_driver.gab_post(USER, PASS, "test", jpg_path=SMALL_IMG, dry_run=True)

    def test_dryrun_posting_with_image(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        gab_driver.gab_post(USER, PASS, "test", dry_run=True)

    @unittest.skip("Live testing disabled")
    def test_live_posting(self) -> None:
        """Tests that gab_post works"""
        gab_driver.gab_post(USER, PASS, "test", dry_run=False)


if __name__ == "__main__":
    unittest.main()
