"""
    BigLeague rss2gab app.
"""

# pylint: disable=R0801,line-too-long

import argparse

from rss2gab import run

RSS_FEED_URL = "http://blast.video/assets/json/trending.rss"
GAB_ID = "testgabposter"
GAB_LOGIN_USER = "testgabposter"
GAB_PASSWORD = "Yq4F2H9Lvp"

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "--published_hours_ago",
    type=int,
    help="How many hours ago to look for new posts from the rss feed.",
    default=24,
)
args = argparser.parse_args()
print("\nRss2Gab BigLeague tester app. Copyright 2022 Zach Vorhies.\n")


run(
    rss_feed_url=RSS_FEED_URL,
    gab_id=GAB_ID,
    gab_login_user=GAB_LOGIN_USER,
    gab_login_pass=GAB_PASSWORD,
    published_hours_ago=args.published_hours_ago,
    headless=True,
)
