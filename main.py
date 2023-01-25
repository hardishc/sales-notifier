# selenium 4
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

options = FirefoxOptions()
#options.headless = True
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)

#driver.get("https://www.garageclothing.com/ca/p/perfect-puffer-matte-jacket/0796161.html?&&utm_campaign=grg-perf-max-can-en&utm_source=google&utm_medium=cpc&utm_term=-&gclid=EAIaIQobChMIzrSf3Zzh_AIVem1vBB1BewuAEAYYASABEgI6pPD_BwE")
#driver.get("https://www.amazon.ca/gp/product/B09DPLXHKH/ref=ox_sc_act_title_1?smid=ASWMM7BDGBZWM&psc=1")
#driver.get("https://www2.hm.com/en_ca/productpage.0875217034.html")
#driver.get("https://www.hollisterco.com/shop/ca/p/curvy-high-rise-flare-jeans-50419711?seq=06&categoryId=12552&faceout=model")
#driver.get("https://www.abercrombie.com/shop/ca/p/mixed-fabric-curve-love-ultra-high-rise-ankle-straight-jean-51389870?seq=29&categoryId=12261&faceout=model")
#driver.get("https://oldnavy.gapcanada.ca/browse/product.do?pid=506760013&cid=1185415&pcid=1031099&vid=1#pdp-page-content")
#driver.get("https://www.ikea.com/ca/en/p/knarrevik-nightstand-black-30381183/")
driver.get("https://www.zara.com/ca/en/trf-mom-fit-comfort-jeans-p08197031.html?v1=222770189&v2=2187589")

sleep(4)
price = driver.find_elements(By.XPATH, "//*[contains(@class, 'Price') or contains(@class, 'price') or contains(@class, 'Pricing') or contains(@class, 'pricing') or contains(@class, 'money') or contains(@class, 'Money')]")

for i in price:
    print(i.text)
    break

driver.quit()
