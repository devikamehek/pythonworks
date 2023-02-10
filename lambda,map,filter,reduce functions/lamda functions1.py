"""A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression."""
"""syntax:  lambda arguments : expression"""

x = lambda a : a + 10
print(x(5))

a=lambda b : b-5
print(a(9))

"""Lambda functions can take any number of arguments"""
x=lambda a,b: a*b
print(x(5,10))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

"""The power of lambda is better shown when you use them as an anonymous function inside another function"""

def myfunc(n):
    return lambda a: a*n

my_dubbler=myfunc(2)
print(my_dubbler(6))