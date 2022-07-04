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

def get_iexcloudapi_data(ticker):
	url = "https://cloud.iexapis.com/stable/stock/{}/quote?token=pk_ef07cccc0b364ebaa4b28740e91d3621".format(ticker)
	response = requests.get(url)
	return response.json()