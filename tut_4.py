from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriver"


driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com")
#article_count = driver.find_element_by_css_selector("#articlecount a")
#article_count.click()

#all_portals = driver.find_element_by_link_text("All portals")
#all_portals.click()

#search_bar = driver.find_element_by_name("search")
#search_bar.send_keys("python")
#search_bar.send_keys(Keys.ENTER)

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

button = driver.find_element_by_class_name("btn-block")

fname.send_keys("Aditya")
lname.send_keys("Shankar")
email.send_keys("apra8001@yahoo.co.in")

button.send_keys(Keys.ENTER)
