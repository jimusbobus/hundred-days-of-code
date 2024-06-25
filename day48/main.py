from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

URL = f"https://www.python.org/"

wd = webdriver.Chrome(options)
wd.get(URL)

# whole = wd.find_element(By.CLASS_NAME, "a-price-whole")
# decimal = wd.find_element(By.CLASS_NAME, "a-price-decimal")
#
# price = float(f"{whole.text}.{decimal.text}")

events = wd.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
print(len(events))
event_array = []

for event in events:
    date = event.find_element(By.TAG_NAME, 'time')
    name = event.find_element(By.TAG_NAME, 'a')
    event_array.append({
        'time': date.text,
        'name': name.text
    })

print(event_array)
wd.quit()
