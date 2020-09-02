from django.test import TestCase
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://127.0.0.1:8000/calc/")

#Identificar elementos usar box para campos a completar y button para botones
entrada_box = driver.find_element_by_name("query")
#Acción con elementos
entrada_box.send_keys("2+2")
entrada_box.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#submit_button.click()
#resultado_box = driver.find_element_by_name("query")
resultado_box = driver.find_element_by_name("resultado")
valor = resultado_box.get_attribute("value")
assert valor == "2+2=4"
#time.sleep(5)
driver.quit()
