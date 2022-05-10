"""
    Generic rss2gab app.
"""

# pylint: disable=R0801

from rss2gab.command import run

headless = "y" in input("Headless? (y/n)?: ").lower()

run(headless=headless)
