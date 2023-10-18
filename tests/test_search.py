import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context(record_video_dir="reports/videos/")
    page = context.new_page()
    page.goto("https://www.amazon.com.br/")
    page.locator('id=twotabsearchtextbox').fill('Yoda')
    page.locator('id=nav-search-submit-button').click()
    page.screenshot(timeout=1000)
    page.locator('id=twotabsearchtextbox').fill('Darth Vader')
    page.locator('id=nav-search-submit-button').click()

    # Make sure to close, so that videos are saved.
    context.close()
    browser.close()
