
# Question 1: Extract Tesla stock data using yfinance
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download Tesla stock data
tesla_data = yf.download('TSLA', start='2010-01-01', end='2023-12-31')
tesla_data.reset_index(inplace=True)
tesla_data.to_csv("tesla_stock_data.csv", index=False)

# Question 2: Extract Tesla revenue data using web scraping
import requests
from bs4 import BeautifulSoup

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in table.text:
        df_list = pd.read_html(str(table))
        tesla_revenue = df_list[0]
        break

# Clean revenue table
tesla_revenue = tesla_revenue.dropna()
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "").str.replace(",", "")
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].astype(float)
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])
tesla_revenue.to_csv("tesla_revenue.csv", index=False)

# Question 3: Plot Tesla stock price and revenue over time
plt.figure(figsize=(12, 5))
plt.plot(tesla_data["Date"], tesla_data["Close"], label="Stock Price")
plt.title("Tesla Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(tesla_revenue["Date"], tesla_revenue["Revenue"], label="Revenue", color="green")
plt.title("Tesla Quarterly Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue (USD)")
plt.legend()
plt.grid()
plt.show()

# Question 4: Extract GameStop stock data using yfinance
gme_data = yf.download("GME", start="2010-01-01", end="2023-12-31")
gme_data.reset_index(inplace=True)
gme_data.to_csv("gme_stock_data.csv", index=False)

# Question 5: Plot GameStop stock price
plt.figure(figsize=(12, 5))
plt.plot(gme_data["Date"], gme_data["Close"], label="Stock Price", color="orange")
plt.title("GameStop Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.legend()
plt.grid()
plt.show()

# Question 6: Extract GameStop revenue data using web scraping
url_gme = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
response_gme = requests.get(url_gme, headers=headers)
soup_gme = BeautifulSoup(response_gme.text, "html.parser")

tables_gme = soup_gme.find_all("table")
for table in tables_gme:
    if "GameStop Quarterly Revenue" in table.text:
        df_gme = pd.read_html(str(table))
        gme_revenue = df_gme[0]
        break

# Clean GME revenue table
gme_revenue = gme_revenue.dropna()
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$", "").str.replace(",", "")
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]
gme_revenue["Revenue"] = gme_revenue["Revenue"].astype(float)
gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])
gme_revenue.to_csv("gme_revenue.csv", index=False)

# Plot GameStop revenue
plt.figure(figsize=(12, 5))
plt.plot(gme_revenue["Date"], gme_revenue["Revenue"], label="Revenue", color="purple")
plt.title("GameStop Quarterly Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue (USD)")
plt.legend()
plt.grid()
plt.show()
