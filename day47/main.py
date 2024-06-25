import requests
from bs4 import BeautifulSoup
from library.SendMessage import send_email


def get_current_price_of_item(url):
    headers = {
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    price_from_html = soup.find_all('span', class_="aok-offscreen")
    return float(price_from_html[0].getText().replace("£", ""))


URL = f"https://www.amazon.co.uk/Heston-Blumenthal-Precision-Platforms-Aquatronic/dp/B00DW419G0/?th=1"
price = get_current_price_of_item(URL)
print(price)

target_price = 50.00

if price < target_price:
    send_email(subject="Shop now, price has dropped", msg=URL)


