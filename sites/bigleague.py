import os

os.system(
    'rss2gab --rss_feed_url "http://Bigleaguepolitics.com/feed" '
    "--gab_id bigleaguepol --gab_login_user Admin@bigleaguepolitics.com "
    "--dry-run"
)
