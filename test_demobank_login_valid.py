from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
    page.locator("#login_id").fill("12345678")
    page.locator("#login_id").press("Enter")
    page.locator("#login_password").click()
    page.locator("#login_password").fill("12345678")
    page.locator("#login_password").press("Enter")

    assert page.inner_text('#user_name') == 'Jan Demobankowy'

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
