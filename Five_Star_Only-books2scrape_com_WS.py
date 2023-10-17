import requests
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get('http://books.toscrape.com/catalogue/category/books_1/index.html')

results = []
product_pods = driver.find_elements(By.CLASS_NAME, 'product_pod')

for product_pod in product_pods:
    star_rating = product_pod.find_element(By.CLASS_NAME, 'star-rating').get_attribute('class')
    if 'Five' in star_rating:
        name = product_pod.find_element(By.XPATH, './/h3/a').get_attribute('title')
        results.append(name)


for title in results:
    print(title)

driver.quit()


print('gg')