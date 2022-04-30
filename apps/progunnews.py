"""
    ProGunNews rss2gab app.
"""


from rss2gab import run

RSS_FEED_URL = "https://progunnews.com/index.rss"
GAB_ID = "ProGunNews"
GAB_LOGIN_USER = "ProGunNews1776@gmail.com"

run(
    rss_feed_url=RSS_FEED_URL,
    gab_id=GAB_ID,
    gab_login_user=GAB_LOGIN_USER,
)
