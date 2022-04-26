"""
    Tests the gab driver.
"""
import unittest

from rss2gab import gab_driver

USER = "blastvideo"
PASS = "nAn8mR4mn6"


class GabDriverTest(unittest.TestCase):
    """Gab driver test framework."""
    def test_posting(self) -> None:
        """Tests that gab_post works"""
        gab_driver.gab_post(USER, PASS, "test", dry_run=True)


if __name__ == "__main__":
    unittest.main()
