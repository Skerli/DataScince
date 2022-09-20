#!/usr/local/bin/python3

import sys

def all_stocks():

	if len(sys.argv) != 2:
		return

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

	if len(sys.argv) != 2:
		return
	
	strr = (sys.argv[1])
	strr = strr.replace(' ', '').split(",")
	print(strr)

if __name__ == '__main__':
	all_stocks()