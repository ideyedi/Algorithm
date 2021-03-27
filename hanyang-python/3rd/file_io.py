#!/bin/python

f_name = open('untitle.txt', 'r', encoding='utf-8')
# func : read(). readlines(), readline()
data = f_name.readline().strip()
f_name.close()
print(data)


w = open('untitle.txt', 'w', encoding='UTF-8')
w.write('Python programming\n')
w.close
