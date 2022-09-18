#!/usr/local/bin/python3

import sys

def stock_prices():
	COMPANIES = {
		'Apple': 'AAPL',
		'Microsoft': 'MSFT',
		'Netflix': 'NFLX',
		'Tesla': 'TSLA',
		'Nokia': 'NOK'
	}
	STOCKS = {
		'AAPL': 287.73,
		'MSFT': 173.79,
		'NFLX': 416.90,
		'TSLA': 724.88,
		'NOK': 3.37
	}

	if (len(sys.argv) == 2):
		var = sys.argv[1]
		var = var.lower().title()
		if var in COMPANIES:
			print(STOCKS[COMPANIES[var]])
		else:
			print('Unknown company')

if __name__ == '__main__':
	stock_prices()