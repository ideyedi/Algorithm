#!/bin/python

price = int(input())

if price >= 300000:
	discount = 10
elif price < 300000 and price >= 50000:
	discount = 7.5
elif price < 50000 and price >= 10000:
	discount = 5
else: 
	discount = 0

print("구매금액 : ", price)
print("할인율   : ", discount)
print("할인 금액: ", price * discount / 100)
print("지불 금액: ", price - price * discount / 100 )
