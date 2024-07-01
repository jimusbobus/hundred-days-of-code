from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

wd = webdriver.Chrome(options)

URL = f"https://www.speedtest.net/"
wd.get(URL)

# Wait for the cookies popup to appear
wait = WebDriverWait(wd, 5)
# Note: Update the selector below to match the actual button you need to click
cookies_accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="I Accept"]')))
# Click the button to accept cookies
cookies_accept_button.click()

go_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'js-start-test')))
go_element.click()


wait = WebDriverWait(wd, 60)
complete = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Result ID"]')))

download_speed = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'download-speed')))
upload_speed = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'upload-speed')))

print(download_speed.text)
print(upload_speed.text)

wd.quit()
