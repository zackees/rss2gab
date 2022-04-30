"""
    BigLeague rss2gab app.
"""

import argparse

from rss2gab import run

RSS_FEED_URL = "http://Bigleaguepolitics.com/feed"
GAB_ID = "bigleaguepol"
GAB_LOGIN_USER = "Admin@bigleaguepolitics.com"
DRY_RUN = True  # Turn off when app is ready

argparser = argparse.ArgumentParser()
argparser.add_argument("--password", help="Password for gab.com account")
args = argparser.parse_args()

run(
    rss_feed_url=RSS_FEED_URL,
    gab_id=GAB_ID,
    gab_login_user=GAB_LOGIN_USER,
    gab_login_pass=args.password,
    dry_run=DRY_RUN,
)
