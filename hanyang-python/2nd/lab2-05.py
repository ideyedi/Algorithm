#!/bin/python

print('-------------------------------------')
print('      cm      mm      m      inch    ')
print('-------------------------------------')

for num in range (1, 101):
	text = '     {cm}     {mm}     {m}      {inch}     '
	text.format(cm=num, mm=num*10, m=num*0.1, inch=num*0.3937)
	print(text)

print('-------------------------------------')
