"""
Command line handler for the rss2gab.
"""

# pylint: disable=line-too-long

import argparse
import sys

import requests  # type: ignore

from rss2gab import rss2gab_loop

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"


def fetch(url: str, timeout: int = 5) -> requests.Response:
    """Fetch a url using the specified user agent."""
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, allow_redirects=True, headers=headers, timeout=timeout)
    return resp


def main() -> None:
    """Command line interface for rss2gab"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter, description="Helper for rss2gab"
    )
    parser.add_argument(
        "--rss_feed_url",
        type=str,
        help="The rss feed, for example: http://Bigleaguepolitics.com/feed",
    )
    parser.add_argument("--gab_id", type=str, help="The gab id, for example gab.com/ID")
    parser.add_argument("--gab_login_user", type=str, help="user name or email used to login")
    parser.add_argument("--gab_login_pass", type=str, help="password used to login")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Optional, when true no posts are made.",
    )
    args = parser.parse_args()
    rss_feed_url = args.rss_feed_url or input("Rss feed url: ")

    print(f"Checking url: {rss_feed_url} ...")
    try:
        resp = fetch(rss_feed_url)
        resp.raise_for_status()
        print(f"The url: {rss_feed_url} is live.")
    except requests.exceptions.MissingSchema:
        print(f'Error: the url "{rss_feed_url}" is malformed url, aborting')
        sys.exit(1)
    except requests.exceptions.RequestException:
        if (
            "y"
            not in input(
                f'Error: the url "{rss_feed_url}" is not live, continue anyway? (y/n): '
            ).lower()
        ):
            sys.exit(1)

    gab_id = args.gab_id or input("Gab id: ")

    gab_id_url = f"https://gab.com/{gab_id}"
    print(f"Checking gab id: {gab_id_url} ...")
    try:
        resp = fetch(gab_id_url)
        resp.raise_for_status()
        print(f"The gab id: {gab_id_url} is live.")
    except Exception:  # pylint: disable=broad-except
        msg = f'Error: the gab id "{gab_id}" is not valid. Continue anyway? (y/n): '
        if "y" not in input(msg).lower():
            sys.exit(1)
        sys.exit(1)
    gab_login_user = args.gab_login_user or input("Gab login user: ")
    gab_login_pass = args.gab_login_pass or input("Gab login pass: ")
    # TODO: validate user/pass on gab.  # pylint: disable=W0511
    rss2gab_loop(rss_feed_url, gab_id, gab_login_user, gab_login_pass, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
