from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Create directories for VRT
directories = ["vrt-actual", "vrt-expected", "vrt-difference"]
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://vshkodin.com/")

# Maximize window (optional)
driver.maximize_window()

# Take screenshot and save it in 'vrt-actual' folder
driver.save_screenshot("vrt-actual/vshkodin_screenshot.png")

# Close the browser
driver.quit()

print("Screenshot saved in vrt-actual folder")
