from playwright.sync_api import Page


def test_search(page: Page) -> None:
    page.goto("https://www.google.com")

