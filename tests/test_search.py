import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    # Make sure to close, so that videos are saved.
    context.close()
    browser.close()