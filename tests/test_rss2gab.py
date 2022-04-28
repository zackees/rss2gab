"""
    Tests parsing an rss feed.
"""
import re
import unittest
from pprint import pprint
from typing import List, Optional, Tuple

from gabposter import gab_post
from rss2gab.gab_readposts import gab_readposts
from rss2gab.parse_rss_feed import RssEntry, parse_rss_feed

# from rss2gab import gab_driver

RSS_FEED = "http://Bigleaguepolitics.com/feed"

USER = "testgabposter"
PASS = "Yq4F2H9Lvp"

POST_IMAGE = False

ACCOUNT = "bigleaguepol"


def _filter_rss_from_existing_posts(
    rss_feed: List[RssEntry], gab_posts: List[str]
) -> List[RssEntry]:
    """
    Filter out the posts that already exist in Gab.
    """
    filtered_rss = []
    for rss_entry in rss_feed:
        content = rss_entry.content
        # Use a regular expression to find the url in the content.
        # This is a bit hacky, but it works.
        url_match = re.search(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            content,
        )
        if not url_match:
            # No url found in the content so assume this is a user post and skip.
            continue
        url = url_match.group(0)
        found = False
        for post in gab_posts:
            if url in post:
                found = True
                break
        if found:
            # Skip, we've already posted this
            continue
        if rss_entry.content not in gab_posts:
            filtered_rss.append(rss_entry)
    return filtered_rss


class RssTester(unittest.TestCase):
    """Gab driver test framework."""

    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        rss_content_list = parse_rss_feed(RSS_FEED)
        gab_posts = gab_readposts(USER)

        filtered_rss = _filter_rss_from_existing_posts(rss_content_list, gab_posts)
        # pprint(filtered_rss)
        # print("done!")
        pprint(filtered_rss)
        # filtered_rss.reverse()
        # for rss_entry in filtered_rss:
        #    gab_post(USER, PASS, rss_entry.content)


if __name__ == "__main__":
    unittest.main()
