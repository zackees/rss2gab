"""
    ProGunNews rss2gab app.
"""

# pylint: disable=R0801,line-too-long

import argparse
import time

from rss2gab import run

RSS_FEED_URL = "https://progunnews.com/index.rss"
GAB_ID = "ProGunNews"
GAB_LOGIN_USER = "ProGunNews1776@gmail.com"

argparser = argparse.ArgumentParser()
argparser.add_argument("--password", help="Password for gab.com account")
argparser.add_argument(
    "--published_hours_ago",
    type=int,
    help="How many hours ago to look for new posts from the rss feed.",
    default=24,
)
args = argparser.parse_args()
print("\nRss2Gab Progunnews app. Copyright 2022 Zach Vorhies.\n")
if args.password is None:
    print(
        '\nNote: avoid entering a password by adding '
        '"--password <MYPASSWORD>" when running this command.\n'
    )
    time.sleep(3)

run(
    rss_feed_url=RSS_FEED_URL,
    gab_id=GAB_ID,
    gab_login_user=GAB_LOGIN_USER,
    gab_login_pass=args.password,
    published_hours_ago=args.published_hours_ago,
    headless=True,
)
