"""
    BigLeague rss2gab app.
"""

# pylint: disable=R0801

import argparse
import time

from rss2gab import run

RSS_FEED_URL = "http://Bigleaguepolitics.com/feed"
GAB_ID = "bigleaguepol"
GAB_LOGIN_USER = "Admin@bigleaguepolitics.com"
DRY_RUN = False  # Turn off when app is ready

argparser = argparse.ArgumentParser()
argparser.add_argument("--password", help="Password for gab.com account")
argparser.add_argument(
    "--published_hours_ago",
    type=int,
    help="How many hours ago to look for new posts from the rss feed.",
    default=24,
)
args = argparser.parse_args()
print("\nRss2Gab BigLeague app. Copyright 2022 Zach Vorhies.\n")
if args.password is None:
    print(
        "\nNote: avoid entering a password by adding "
        '"--password <MYPASSWORD>" when running this command.\n'
    )
    time.sleep(3)

if DRY_RUN:
    print(
        "\nThis app is a demo. It will not actually post anything to gab.com."
        " Also the full app will run silently rather than pop up a web window.\n"
    )
    time.sleep(3)

run(
    rss_feed_url=RSS_FEED_URL,
    gab_id=GAB_ID,
    gab_login_user=GAB_LOGIN_USER,
    gab_login_pass=args.password,
    published_hours_ago=args.published_hours_ago,
    headless=not DRY_RUN,
    dry_run=DRY_RUN,
)
