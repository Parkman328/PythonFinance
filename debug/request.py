import requests, datetime

def print_my_request(r):
    print('method:{} Type:{}'.format(method,type(r)))
    print('Output: {}'.format(r.text))
    
end_date = datetime.date.today()
one_day = datetime.timedelta(days=1)
end_date = end_date - one_day
delta = datetime.timedelta(days=7)
start_date = end_date - delta

method ='get_ticker_data'
url = 'http://localhost:5000/'+method

#r = requests.post(url, json={'data':'DOCU', 'start_date': start_date.strftime("%Y, %m, %d"),'end_date': end_date.strftime("%Y, %m, %d")})
#print_my_request(r)



method ='get_ticker_closing'
url = 'http://localhost:5000/'+method
#r = requests.post(url, json={'data':'DOCU', 'start_date': start_date.strftime("%Y, %m, %d"),'end_date': end_date.strftime("%Y, %m, %d")})
#print_my_request(r)

method ='get_tickers'
url = 'http://localhost:5000/'+method
print(url)
r = requests.post(url, json={'data':'DOCU, SHOP, WMT', 'start_date': start_date.strftime("%Y, %m, %d"),
                            'end_date': end_date.strftime("%Y, %m, %d"), 'attrib':'yahoo'})
print_my_request(r)

method ='get_Percent_change'
url = 'http://localhost:5000/'+method
print(url)
r = requests.post(url, json={'data':'DOCU, SHOP, WMT', 'start_date': start_date.strftime("%Y, %m, %d"),
                             'end_date': end_date.strftime("%Y, %m, %d"), 'attrib':'yahoo'})
print_my_request(r)

method ='get_Mean_Daily_Return'
url = 'http://localhost:5000/'+method
print(url)
r = requests.post(url, json={'data':'DOCU, SHOP, WMT', 'start_date': start_date.strftime("%Y, %m, %d"),
                             'end_date': end_date.strftime("%Y, %m, %d"), 'attrib':'yahoo'})
print_my_request(r)

method ='get_Cov_Matrix'
url = 'http://localhost:5000/'+method
print(url)
r = requests.post(url, json={'data':'DOCU, SHOP, WMT', 'start_date': start_date.strftime("%Y, %m, %d"),
                             'end_date': end_date.strftime("%Y, %m, %d"), 'attrib':'yahoo'})
print_my_request(r)

method ='simulate_random_portfolios'
url = 'http://localhost:5000/'+method
print(url)
r = requests.post(url, json={'data':'DOCU, SHOP, ZM', 'start_date': start_date.strftime("%Y, %m, %d"),
                             'end_date': end_date.strftime("%Y, %m, %d"), 'attrib':'yahoo',
                             'num_portfolios':10, 'rf':0.0})
print_my_request(r)