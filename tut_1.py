from selenium import webdriver
# you need to install the selenium library and the web_browser-driver (ex: chrome, safari, firefox etc.)

chrome_driver_path = "chromedriver"

# create a new web driver and provide the path to the executable file
driver = webdriver.Chrome(chrome_driver_path)
# procedure : how to fetch a specific url from the from world wide web.
driver.get("https://www.amazon.in/")
