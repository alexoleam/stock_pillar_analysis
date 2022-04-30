import requests

headers = {
	
	'Content-Type': 'application/json',
	'Authorization': 'Token '
}

def get_meta_data(ticker):
	url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
	response = requests.get(url, headers=headers)
	return response.json()

def get_price_data(ticker):
	url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
	response = requests.get(url, headers=headers)
	response = response.json()[0]
	response['marketCap'] = response['volume']*response['open']
	return response

def get_statement_data(ticker):
	url = "https://api.tiingo.com/tiingo/fundamentals/{}/statements".format(ticker)
	response = requests.get(url, headers=headers)
	return response.json()[0]

def get_historical_data(ticker):
	url = "https://api.tiingo.com/tiingo/fundamentals/{}/statements".format(ticker)
	response = requests.get(url, headers=headers)
	return response.json()[slice(6)]