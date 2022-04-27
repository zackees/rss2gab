"""
    Module for interacting with the Gab.com website.
"""

import ssl

from autoselenium import Driver  # type: ignore
from selenium.webdriver.common.action_chains import ActionChains  # type: ignore

ssl._create_default_https_context = (  # pylint: disable=protected-access
    ssl._create_unverified_context  # pylint: disable=protected-access
)

# Tested to work. For some reason the test fails if it's less resolution than this.
WIDTH = 1200
HEIGHT = 800


def _action_login(driver: Driver, username: str, password: str) -> None:
    """Logs into Gab.com and posts the given content."""
    # Handle Page sign in, where the user and password are entered.
    driver.get("https://gab.com/auth/sign_in")
    el_email = driver.find_element_by_id("user_email")
    el_email.click()
    el_email.send_keys(username)
    el_password = driver.find_element_by_id("user_password")
    el_password.click()
    el_password.send_keys(password)
    el_submit_btn = driver.find_element_by_name("button")
    el_submit_btn.click()


def _action_make_post(driver: Driver, content: str, dry_run: bool) -> None:
    """Makes a social media post"""
    driver.get("https://gab.com/compose")
    el_compose_window = driver.find_element_by_css_selector("div.DraftEditor-root")
    el_compose_window.click()
    # Now use the keyboard to enter in the content.
    actions = ActionChains(driver)
    actions.send_keys(content)
    actions.perform()
    # Find an element that contains "Post"
    el_post_btn = driver.find_element_by_xpath('//*[contains(text(), "Post")]')
    # put the mouse over the button of el_post_btn and click it.
    actions = ActionChains(driver)
    actions.move_to_element(el_post_btn)
    actions.click()
    if not dry_run:
        actions.perform()


def gab_post(username: str, password: str, content: str, dry_run: bool = False) -> None:
    """Logs into Gab.com and posts the given content."""
    with Driver("firefox", root="drivers") as driver:
        driver.delete_all_cookies()
        driver.set_window_size(WIDTH, HEIGHT)
        _action_login(driver, username, password)
        _action_make_post(driver, content, dry_run)
