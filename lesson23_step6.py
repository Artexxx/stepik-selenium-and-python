from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)


button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(0.5)


new_window = browser.window_handles[1]
browser.switch_to_window(new_window)


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)


input = browser.find_element_by_id("answer")
input.send_keys(y)


button = browser.find_element_by_class_name("btn.btn-primary")
button.click()
