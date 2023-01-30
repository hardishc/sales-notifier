# selenium 4
from selenium import webdriver
import re
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


def current_price(file):
    for item in file:
        comma_index = item.index(',')
        item_url = item[0:comma_index]

        if item_url == "url":
            continue

        item_price = item[comma_index+1:]

        driver.get(item_url)        

        new_price = driver.find_elements(By.XPATH, "//*[contains(@class, 'Price') or contains(@class, 'price') or contains(@class, 'Pricing') or contains(@class, 'pricing') or contains(@class, 'money') or contains(@class, 'Money')]")

        for i in new_price:            
            x = re.search("([0-9]+\.[0-9].)", i.text) or re.search("([0-9]+)", i.text)
            print(x.group())            
            break
            

        



options = FirefoxOptions()
#options.headless = True
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)

file = open("price.csv", "r")

current_price(file)

#driver.get("https://www.ikea.com/ca/en/p/knarrevik-nightstand-black-30381183/")



sleep(4)
#price = driver.find_elements(By.XPATH, "//*[contains(@class, 'Price') or contains(@class, 'price') or contains(@class, 'Pricing') or contains(@class, 'pricing') or contains(@class, 'money') or contains(@class, 'Money')]")

driver.quit()
