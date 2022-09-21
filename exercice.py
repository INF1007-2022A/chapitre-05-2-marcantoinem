#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	cost = 0
	for _, item_qt, price in data:
		cost += item_qt*price

	print(name)
	print("SOUS TOTAL    {0:.2f} $".format(cost))
	print("TAXES         {0:.2f} $".format(cost * 0.15))
	print("TOTAL         {0:.2f} $".format(cost * 1.15))


def format_number(number, num_decimal_digits):
	return "{0:.{1}f}".format(number, num_decimal_digits)

def get_triangle(num_rows):
	total_size = num_rows * 2 + 1
	triangle = "".join("+" for i in range(total_size)) + "\n"
	for row in range(num_rows):
		triangle += "+"
		space = num_rows - row - 1
		triangle += "".join(" " for i in range(space))
		a = total_size - 2*space - 2
		triangle += "".join("A" for i in range(a))
		triangle += "".join(" " for i in range(space))
		triangle += "+\n"
	triangle += "".join("+" for i in range(total_size))
	return triangle


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
