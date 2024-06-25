from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

URL = f"https://en.wikipedia.org/wiki/Main_Page"

wd = webdriver.Chrome(options)
wd.get(URL)

article_count = wd.find_element(By.CSS_SELECTOR, "#articlecount a")

print(article_count.text)

wd.quit()
