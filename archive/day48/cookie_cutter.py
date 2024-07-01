from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from typing import List

from selenium.webdriver.remote.webelement import WebElement


def has_five_seconds_passed(_start_time):
    current_time = time.time()
    return current_time - _start_time >= 2.66


def buy_most_expensive(elements: List[WebElement]):
    most_expensive_element = None
    highest_cost = 0
    for element in elements[::-1]:
        try:
            if element.is_displayed() and (element.get_attribute("class") == ""):
                element.click()
                # print(element.get_attribute("class"))
                # print(element.get_attribute("id"))
        except AttributeError as e:
            print("Attribute error, continue")
        except StaleElementReferenceException as e:
            print("StaleElementReferenceException, continue")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

URL = "http://orteil.dashnet.org/experiments/cookie/"

wd = webdriver.Chrome(options)
wd.get(URL)

money = 0
time_seconds = time.time()
start_time = time.time()
cps = None
# How many seconds the while loop should run
duration = 5 * 60  # 5 minutes converted to seconds
# Loop until the current time is 5 minutes greater than the start time
while time.time() < start_time + duration:
    cookie = wd.find_element(By.ID, "cookie")
    cps = wd.find_element(By.ID, "cps")
    cookie.click()
    cookie.click()
    money = int(wd.find_element(By.ID, "money").text.replace(",", ""))
    if has_five_seconds_passed(time_seconds):
        print("At least 3 seconds have passed.")
        store = wd.find_element(By.ID, "store")
        can_buy = store.find_elements(By.XPATH, '//*[@id="store"]/div[@onclick]')
        buy_most_expensive(can_buy)
        time_seconds = time.time()

print(cps.text)

wd.quit()
