import requests

headers = {
	
	'Content-Type': 'application/json',
	'Authorization': 'Token '
}

def get_meta_data(ticker):
	url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
	response = requests.get(url, headers=headers)
	return response.json()