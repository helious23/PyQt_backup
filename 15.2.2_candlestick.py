import pandas_datareader.data as web
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance.original_flavor as mpf
import matplotlib.ticker as ticker

yf.pdr_override()

sk_hynix = web.get_data_yahoo("000660.KS", start="2024-02-01", end="2024-03-18")

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

name_list = []
day_list = []

for i, day in enumerate(sk_hynix.index):
    if day.dayofweek == 0:
        day_list.append(i)
        name_list.append(day.strftime("%Y-%m-%d") + "(Mon)")

ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

mpf.candlestick2_ohlc(
    ax,
    sk_hynix["Open"],
    sk_hynix["High"],
    sk_hynix["Low"],
    sk_hynix["Close"],
    width=0.5,
    colorup="r",
    colordown="b",
)
plt.grid()
plt.show()
