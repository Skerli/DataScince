#!/usr/local/bin/python3

class Must_read:
	with open('data.csv', 'r', encoding='utf-8') as file:
		print(file.read())

if __name__ == '__main__':
	Must_read