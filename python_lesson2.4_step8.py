import time, math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

button = browser.find_element_by_css_selector("button#book")
if WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    ):
    button.click()

x_element = browser.find_element_by_css_selector("#input_value.nowrap")
x = x_element.text
y = calc(x)
input = browser.find_element_by_id("answer")
input.send_keys(y)

button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#solve"))
    )
button.click()
time.sleep(35)
assert "successful" in message.text
browser.quit()
