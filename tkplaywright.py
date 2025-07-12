from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Go to a page with a form
    page.goto("https://www.w3schools.com/html/html_forms.asp")

    # Wait for the input field to load
    page.wait_for_selector("input[name='firstname']")

    # Type into the input field
    page.fill("input[name='firstname']", "Tamil")

    print("✅ Typed 'Tamil' into the 'First name' field.")

    # Optional: wait so you can see the result before browser closes
    time.sleep(3)

    # Close browser
    browser.close()

