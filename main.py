# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://www.amazon.ca/COCHOA-Triple-Leather-Womens-Crossbody/dp/B07RY8JQ1D?ref_=Oct_DLandingS_D_de9c8009_62")

price = driver.find_element(By.XPATH, "//*[contains(@class, 'Price') or contains(@class, 'price') or contains(@class, 'Pricing') or contains(@class, 'pricing')]").text

print(price)

driver.quit()