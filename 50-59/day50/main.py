from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

URL = f"https://sketch.io/sketchpad/"

wd = webdriver.Chrome(options)
wd.get(URL)

popup = wd.find_element(By.XPATH, '/html/body/dialog/alertify-dialog/p/div/alert-close-link')
popup.click()

count = 0

while count < 10:
    element_to_swipe = wd.find_element(By.XPATH, '/html/body/sketchpad/sketchpad-viewport/sketch-doc/sketch-doc-scrollarea')

    actions = ActionChains(wd)

    actions.move_to_element_with_offset(element_to_swipe, 0, 5*count)  # Start at the left edge of the element
    actions.click_and_hold()  # Click and hold the mouse button
    actions.move_by_offset(100, 0)  # Move the mouse 100 pixels to the right
    actions.release()  # Release the mouse button to complete the swipe
    actions.perform()
    time.sleep(1)
    count += 1


wd.quit()
