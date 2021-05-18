#!/bin/python

temper = int(input())
value = int(input())

if temper == 1:
	print("Celsius :    ", value)
	print("Fahrenheit : ", value * 9 / 5 + 32)
elif temper == 2:
	print("Celsius :    ", (value - 32)*5/9)
	print("Fahrenheit : ", value)
else:
	print("Invalid value")
