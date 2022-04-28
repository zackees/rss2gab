"""
    Tests the gab driver.
"""
import json
import re
import subprocess
import unittest
from typing import List

import feedparser
from bs4 import BeautifulSoup
from gabposter import gab_post

# from rss2gab import gab_driver


ACCOUNT = "bigleaguepol"
NUMBER_GABS = 100


def gab_readposts(user: str, limit: int = NUMBER_GABS) -> List[str]:
    """Tests that gab_post works, but doesn't not post."""
    cmd = ["garc", "userposts", user, f"--number_gabs={limit}"]
    stdout = subprocess.check_output(cmd, universal_newlines=True)
    lines = stdout.split("\n")
    lines = [line for line in lines if line.startswith("{")]
    titles = []
    for line in lines:
        try:
            data = json.loads(line)
            titles.append(data["body"])
        except Exception as err:  # pylint: disable=broad-except
            print(f"{__file__}: Warning, bad characters in json: {err}, while parsing {line}")
    return titles


class GarcTester(unittest.TestCase):
    """Gab driver test framework."""

    def test_fetch_bigleague(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        posts = gab_readposts(ACCOUNT)
        from pprint import pprint

        pprint(posts)


if __name__ == "__main__":
    unittest.main()
