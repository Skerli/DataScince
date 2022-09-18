#!/usr/local/bin/python3

import string

def read_and_write():
	fd = open('ds.csv', 'r')
	str = fd.read()
	fd.close()
	new = open('ds.tsv', 'w')

	#str = str[:1] + 'T' + str[2:]
	str = str.replace(',', '\t')
	new.write(str)
	new.close()


if __name__ == '__main__':

	read_and_write()