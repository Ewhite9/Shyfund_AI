import requests

# Simple moving average (SMA)
url = 'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=daily&time_period=200&series_type=close&apikey=NGQKTSLQAF79PJFV'
r = requests.get(url)
data = r.json()

# print(data)