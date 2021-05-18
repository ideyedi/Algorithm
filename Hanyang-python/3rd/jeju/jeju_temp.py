# python 3.9.2
#!bin/python

f = open('jeju_2019.csv', 'r', encoding='UTF-8')

while True:
    data = f.readline()
    print(data)

    if data is '':
        break


f.close()
