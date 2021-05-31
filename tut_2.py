from selenium import webdriver

chrome_driver_path = "chromedriver"


driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.amazon.in/OnePlus-Nord-Marble-256GB-Storage/dp/B0869855B8/ref=sr_1_24?dchild=1&qid=1622495352&refinements=p_89%3AOnePlus%7CSamsung&rnid=3837712031&s=electronics&sr=1-24")
# fetch the price of the article and then print it out !
price = driver.find_element_by_id("priceblock_ourprice")

print(price.text)
