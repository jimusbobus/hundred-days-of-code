import requests
from bs4 import BeautifulSoup
import re

from day53.HousePriceForm import HousePriceForm


def convert_currency_to_number(currency_str):
    # Remove dollar sign and other non-numeric characters except for the decimal point
    numeric_str = re.sub(r'[^\d.]', '', currency_str)

    # Convert the string to a float
    return float(numeric_str)


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
properties = []
property_cards = soup.find_all('li', class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
for property_card in property_cards:
    properties.append({
        'address': property_card.find("address").text.strip(),
        'link': property_card.find("a")['href'],
        'price': convert_currency_to_number(
            property_card.find("span", class_="PropertyCardWrapper__StyledPriceLine").text.strip())
    })

form = HousePriceForm()

form.populate_form(properties)

form.quit()
