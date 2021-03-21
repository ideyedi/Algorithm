#!/bin/python

class SimpleTest():
    a = 100

# Magic method
# internal pre defined function
    def __init__(self):
        print('init !!')

    def print_hello_ok(self):
        print('Hello Python3!')
'''
    def print_hello_nok():
        print('Hello python')
'''

simple1 = SimpleTest()
simple1.print_hello_ok()

