import requests, datetime

def print_my_request(r):
    print('method:{} Type:{}'.format(method,type(r)))
    print('Output: {}'.format(r.text))
    
end_date = datetime.date.today()
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
r = requests.post(url, json={'data':'DOCU', 'start_date': start_date.strftime("%Y, %m, %d"),
                             'end_date': end_date.strftime("%Y, %m, %d"),'attrib':'yahoo'})
print_my_request(r)