from selenium import webdriver

chrome_driver_path = "chromedriver"


driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.python.org/")


#search_bar = driver.find_element_by_name("q")
#print(search_bar.get_attribute("placeholder"))

#logo = driver.find_element_by_class_name("python-logo")
#print(logo.size)

#link = driver.find_element_by_css_selector(".documentation-widget a")
#print(link.text)

#wiki_link = driver.find_element_by_xpath('//*[@id="container"]/li[4]/ul/li[10]/a')
#print(wiki_link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
times = []
for time in event_times:
    times.append(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
names = []
for name in event_names:
    names.append(name.text)

dictionary = dict(zip(names, times))

print(dictionary)
driver.quit()
