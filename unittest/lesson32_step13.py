from selenium import webdriver
import time
import unittest


class test_reg_page(unittest.TestCase):
	def test_registration_page_1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
		input1.send_keys("Ivan")

		input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
		input2.send_keys("Petrov")

		input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
		input3.send_keys("Smolensk")


		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)


		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Registration page #1 — not passed")

        
	def test_registration_page_2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
		input1.send_keys("Ivan")

		input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
		input2.send_keys("Petrov")

		input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
		input3.send_keys("Smolensk")


		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)


		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Registration page #2 — not passed")


if __name__ == '__main__':
	unittest.main()
