
# Question 1: Extract Tesla stock data using yfinance
!pip install yfinance
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.head()

# Question 2: Extract Tesla revenue data using web scraping
# Send request with headers to bypass 403
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in table.text:
        revenue_table = table
        break
# Extract revenue data into DataFrame        
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in revenue_table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue != "":
            tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

tesla_revenue.tail()

# Question 3: Extracting Gamestop Stock Data using yfinance
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()
# Question 4: Webscraping GME revenue data from Macrotrends
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table")
for table in tables:
    if "GameStop Quarterly Revenue" in table.text:
        revenue_table = table
        break
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in revenue_table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue != "":
            gme_revenue = pd.concat([gme_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

# Show last 5 rows
gme_revenue.tail()


# Question 5 - Tesla Stock and Revenue Dashboard
def make_graph(stock_data, revenue_data, stock_name):
    import matplotlib.pyplot as plt

    # Reset index if needed
    if 'Date' not in stock_data.columns:
        stock_data.reset_index(inplace=True)

    # Convert revenue dates to datetime
    revenue_data['Date'] = pd.to_datetime(revenue_data['Date'])
    revenue_data['Revenue'] = revenue_data['Revenue'].str.replace(",", "").str.replace("$", "").astype(float)

    # Plotting
    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(stock_data['Date'], stock_data['Close'], label='Stock Price', color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stock Price (USD)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(revenue_data['Date'], revenue_data['Revenue'], label='Revenue', color='green')
    ax2.set_ylabel('Revenue (USD)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.title(f"{stock_name} Stock Price and Revenue")
    fig.tight_layout()
    plt.show()

# Question 5
make_graph(tesla_data, tesla_revenue, "Tesla")

# Question 6 - GameStop Stock and Revenue Dashboard

make_graph(gme_data, gme_revenue, "GameStop")
