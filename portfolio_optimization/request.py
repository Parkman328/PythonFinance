import requests

url = 'http://localhost:5000/get_tickers'
r = requests.post(url,json={'GOOG'})

print(r.json())