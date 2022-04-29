"""
    BigLeague rss2gab app.
"""


from rss2gab.command import run

RSS_FEED_URL = "http://Bigleaguepolitics.com/feed"
GAB_ID = "bigleaguepol"
GAB_LOGIN_USER = "Admin@bigleaguepolitics.com"
DRY_RUN = True  # Turn off when app is ready

run(
    rss_feed_url=RSS_FEED_URL,
    gab_id=GAB_ID,
    gab_login_user=GAB_LOGIN_USER,
    dry_run=DRY_RUN,
)
