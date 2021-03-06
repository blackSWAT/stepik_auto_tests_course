import unittest
import time
from selenium import webdriver

class TestAbs(unittest.TestCase):
	def test_firts(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		first = browser.find_element_by_class_name('form-control.first')
		first.send_keys("1")
		second = browser.find_element_by_tag_name('input[placeholder="Input your last name"]')
		second.send_keys("1")
		third = browser.find_element_by_css_selector('div:nth-child(3) input')
		third.send_keys("1")

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!" , welcome_text)
		browser.quit()
	
	def test_two(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		first = browser.find_element_by_class_name('form-control.first')
		first.send_keys("1")
		second = browser.find_element_by_tag_name('input[placeholder="Input your last name"]')
		second.send_keys("1")
		third = browser.find_element_by_css_selector('div:nth-child(3) input')
		third.send_keys("1")

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!" , welcome_text)
		browser.quit()
		
unittest.main()
