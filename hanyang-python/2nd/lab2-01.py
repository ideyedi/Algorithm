#!/bin/python

tall = int(input())
weight = int(input())

if (tall - 100) * 0.9 < weight :
	print("다이어트가 필요합니다.")
else:
	print("정상입니다.")
