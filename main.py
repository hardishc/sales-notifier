# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()

# use headless browsing
#options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get("https://www2.hm.com/en_ca/productpage.0975845001.html")
price = driver.find_element(By.XPATH, "//*[contains(@class,'price') or contains(@class,'Price')]").text
print(price)
driver.quit
