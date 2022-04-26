"""
    Module for interacting with the Gab.com website.
"""

import ssl
import time

from autoselenium import Driver
from selenium.webdriver.common.action_chains import ActionChains

ssl._create_default_https_context = (
    ssl._create_unverified_context  # pylint: disable=protected-access
)

# Tested to work. For some reason the test fails if it's less resolution than this.
WIDTH = 1200
HEIGHT = 800


def gab_post(username: str, password: str, content: str, dry_run=False) -> None:
    """Logs into Gab.com and posts the given content."""
    with Driver("firefox", root="drivers") as driver:
        driver.delete_all_cookies()
        driver.set_window_size(WIDTH, HEIGHT)
        driver.get("https://gab.com/auth/sign_in")
        el_email = driver.find_element_by_id("user_email")
        el_email.click()
        el_email.send_keys(username)
        el_password = driver.find_element_by_id("user_password")
        el_password.click()
        el_password.send_keys(password)
        el_submit_btn = driver.find_element_by_name("button")
        el_submit_btn.click()
        driver.get("https://gab.com/compose")
        time.sleep(5)
        el_compose_window = driver.find_element_by_css_selector("div.DraftEditor-root")
        el_compose_window.click()
        actions = ActionChains(driver)
        actions.send_keys(content)
        actions.perform()
        if dry_run:
            return
        print("make post")
