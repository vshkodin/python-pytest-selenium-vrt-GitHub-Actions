from selenium import webdriver
import os

# Create directories for VRT
directories = ["vrt-actual", "vrt-expected", "vrt-difference"]
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Initialize Chrome WebDriver (Chrome should be installed in the environment)
driver = webdriver.Chrome()

# Open the website
driver.get("https://vshkodin.com/")

# Maximize window (optional)
driver.maximize_window()

# Take screenshot and save it in 'vrt-actual' folder
driver.save_screenshot("vrt-actual/vshkodin_screenshot.png")

# Close the browser
driver.quit()

