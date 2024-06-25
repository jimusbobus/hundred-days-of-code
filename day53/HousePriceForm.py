from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HousePriceForm:
    FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfWiAmCWMlAdICUNbh97ZqdDDI-FJXnxvVxu3f-CZvZvedCEQ/viewform?usp=sf_link"

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options)
        self.driver.get(HousePriceForm.FORMS_URL)

    def populate_form(self, properties):
        for p in properties:
            print(p)
            self.enter_value("What is the Address of the property", p['address'])
            self.enter_value("What is the sale price", p['price'])
            self.enter_value("Whats the ink to the property", p['link'])
            self.click_submit()
            self.enter_another_address()

    def enter_another_address(self):
        wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout
        another_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Submit another response']")))
        another_button.click()

    def click_submit(self):
        wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Submit']")))
        submit_button.click()

    def enter_value(self, entry_title, value):
        wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout
        address_div_element = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f"div[data-params*='{entry_title}']")))
        input_element = address_div_element.find_element(By.TAG_NAME, "input")
        input_element.send_keys(value)

    def quit(self):
        self.driver.quit()
