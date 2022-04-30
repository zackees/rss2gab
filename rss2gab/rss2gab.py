"""
    Tests parsing an rss feed.
"""

# pylint: disable=too-many-arguments

import re
import time
import traceback
from typing import List, Optional

from gabposter import gab_post  # type: ignore

from rss2gab.gab_readposts import gab_readposts
from rss2gab.parse_rss_feed import RssEntry, parse_rss_feed

URL_PATTERN = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


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
        url_match = re.search(URL_PATTERN, content)
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


def rss2gab(
    url_rss_feed: str,
    gab_id: str,
    gab_login_user: str,
    gab_login_pass: str,
    dry_run: bool = False,
    limit: Optional[int] = None,
) -> None:
    """
    Parse the RSS feed and post to Gab.
    """
    print(f"Checking for new posts from {url_rss_feed}")
    rss_content_list = parse_rss_feed(url_rss_feed)
    gab_posts = gab_readposts(
        gab_id, gab_login_user=gab_login_user, gab_login_pass=gab_login_pass
    )
    new_rss_entries = _filter_rss_from_existing_posts(
        rss_content_list, gab_posts
    )
    if not new_rss_entries:
        print("No new posts to post.")
        return
    print(
        f"Found {len(new_rss_entries)} new posts to post on the {gab_id} feed."
    )
    new_rss_entries.reverse()
    if limit is not None:
        new_rss_entries = new_rss_entries[:limit]
    for rss_entry in new_rss_entries:
        print(f"Posting: {rss_entry.content}")
        try:
            gab_post(
                gab_login_user,
                gab_login_pass,
                rss_entry.content,
                dry_run=dry_run,
            )
        except Exception as err:  # pylint: disable=broad-except
            print(f"{__file__}: Error posting because of {err}")
            continue


def rss2gab_loop(
    url_rss_feed: str,
    gab_id: str,
    gab_login_user: str,
    gab_login_pass: str,
    dry_run: bool = False,
    interval: int = 60,
) -> None:
    """
    Parse the RSS feed and post to Gab.
    """
    while True:
        try:
            rss2gab(
                url_rss_feed,
                gab_id,
                gab_login_user,
                gab_login_pass,
                dry_run=dry_run,
            )
            print(f"Sleeping for {interval} seconds.")
        except KeyboardInterrupt:
            break
        except Exception as err:  # pylint: disable=broad-except
            print(f"\nError encountered: {err}\n\nStackTrace:\n")
            traceback.print_exc()
        time.sleep(interval)
