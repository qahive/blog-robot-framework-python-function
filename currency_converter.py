import requests

def convert_usd_to(currency, amount):
	url = 'https://api.exchangerate-api.com/v4/latest/USD'
	response = requests.get(url)
	data = response.json()
	return data['rates'][currency] * float(amount)
