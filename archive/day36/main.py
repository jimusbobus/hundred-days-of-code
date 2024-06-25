import requests
import json
import datetime as dt
from newsapi import NewsApiClient

UP = "🔺"
DOWN = "🔻"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_CHANGE = 0.5

# AVS (Alpha Vantage Stock) - https://www.alphavantage.co/documentation/
AVS_API_KEY = "FIYCF2DHGJT9N1TK"
AVS_URL = "https://www.alphavantage.co/query"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

avs_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": AVS_API_KEY
}
response = requests.get(AVS_URL, params=avs_params)
response.raise_for_status()
avs_data = response.json()
# print(f"DEBUG: AVS Data:\n{json.dumps(avs_data, indent=4)}")
# print(f"DEBUG: AVS Data RAW:\n{avs_data['Time Series (Daily)']}")

# last_trading_date (ltd)
last_trading_date = list(avs_data['Time Series (Daily)'].keys())[0]
# previous_trading_date (ptd)
previous_trading_date = list(avs_data['Time Series (Daily)'].keys())[1]

today = dt.datetime.now().today()
# print(today.date())

closing_value_ltd = float(avs_data['Time Series (Daily)'][last_trading_date]['4. close'])
closing_value_ptd = float(avs_data['Time Series (Daily)'][previous_trading_date]['4. close'])

# print(f"DEBUG: Closing: ltd={closing_value_ltd}, ptd={closing_value_ptd}")

# Percentage change between 2 days.
change_percentage = round(((closing_value_ltd - closing_value_ptd) / closing_value_ltd) * 100, 2)

# print(f"DEBUG: & Change = {change_percentage}")
is_stock_increase = change_percentage > STOCK_CHANGE
is_stock_decrease = change_percentage < (STOCK_CHANGE * -1)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

NEWS_API_KEY = '8d9f3e5819634891adc262dfb5823dc0'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

if is_stock_increase or is_stock_decrease:
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    sources = newsapi.get_sources(language="en", country="gb")
    # print(sources)
    all_articles = newsapi.get_everything(
        q=STOCK, sort_by="relevancy", language="en",
        from_param=last_trading_date, to=previous_trading_date
    )

    msg_article_details = [{'title': article['title'], 'description': article['description'], } for article in
                           all_articles['articles'][:3]]
    with open('msg_template-txt', 'r') as template_file:
        sms_message = template_file.read()
        direction = UP
        if is_stock_decrease:
            direction = DOWN

        for article in msg_article_details:
            sms_message = sms_message.replace('[STOCK]', STOCK)
            sms_message = sms_message.replace('[STOCK_DIRECTION]', direction)
            sms_message = sms_message.replace('[STOCK_CHANGE]', f"{change_percentage}")
            sms_message = sms_message.replace('[TITLE]', article['title'])
            sms_message = sms_message.replace('[DESCRIPTION]', article['description'])

            print(sms_message)

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required 
to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
