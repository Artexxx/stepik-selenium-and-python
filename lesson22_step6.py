from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)


input_scroll = browser.find_element_by_tag_name("input")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_scroll)
time.sleep(1)

input = browser.find_element_by_id("answer")
input.send_keys(y)


option1 = browser.find_element_by_id("robotCheckbox")
option1.click()


option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_tag_name("button")
button.click()