#!/bin/python

f = open('sample.csv', 'r', encoding='UTF-8')

while True:
    line = f.readline().strip()
    if not line:
        break

    columns = line.split(',')
    print(columns)

f.close()

# context manager
with open('sample.csv', 'r', encoding='UTF-8') as f:
    data = f.read()

print(data)
