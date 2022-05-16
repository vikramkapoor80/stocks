import re
from flask import (Flask, render_template, current_app, request, url_for, redirect)
from dotenv import load_dotenv
import requests, os, itertools, json
app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates'
            )


@app.route('/')
def index():
    messages, results, days, average, symbol = [], [], 0, 0, None
    try:
        symbol = os.getenv('SYMBOL', 'MSFT')
        days = os.getenv('NDAYS', 7)
        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey=WBUKE8N4OQFXB3GA")
        response_data = response.json()
        response_data = response_data["Time Series (Daily)"]
        results = dict(itertools.islice(response_data.items(), int(days)))
        average = 0.00
        average = sum(float(response_data[d].get('4. close', 0)) for d in results.keys()) / int(days)
    except Exception as e:
        messages.append(f"An error occurred when trying to retrieve data for {symbol}")
    return render_template('index.html', results=results, days=days, symbol=symbol, average=average,messages=messages)

if __name__ == "__main__":
    load_dotenv()
    debug = os.getenv('DEBUG')
    app.debug = debug
    app.run(host='0.0.0.0', port=80)