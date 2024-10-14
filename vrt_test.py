from playwright.sync_api import sync_playwright

# Initialize Playwright and start it.
playwright = sync_playwright().start()
# Launch the Chromium browser, with headless mode set to False (browser UI will be visible).
browser = playwright.chromium.launch(headless=True)
# self.browser = self.playwright.chromium.launch(headless=False)
# Open a new page (tab) in the browser.
page = browser.new_page()
page.goto("https://vshkodin.com/")
# Take a screenshot and save it to 'vrt-actual' folder
page.screenshot(path="vrt-actual/vshkodin_screenshot.png")
# Close the browser
browser.close()