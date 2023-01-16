# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://www.hollisterco.com/shop/ca/p/oversized-spider-man-graphic-hoodie-47815825?seq=01&categoryId=12635&faceout=model")