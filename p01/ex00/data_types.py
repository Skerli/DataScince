#!/usr/local/bin/python3

def data_types():
	variable = (
		1,
		'sas',
		3.3,
		False,
		[1, 3, 'f'],
		{'first': 1, 'second': 3},
		(1, 'fdsf', 5),
		{1, 3, 5, 2, 5}
	)

	output = '['
	for var in variable:
		output += type(variable).__name__ + ', '
	output = output[:-2] + ']'
	print(output)

if __name__ == '__main__':
	data_types()