"""A decorator is a design pattern in Python that allows a user
to add new functionality to an existing object without modifying its structure.
Decorators are usually called before the definition of a function you want to decorate"""

"""
You'll use a decorator when you need to change the behavior of a function without modifying the function itself
"""
"""
In fact, there are two types of decorators in Python — 
class decorators and function decorators
"""
"""
There are four types of decorators in Angular:
Class Decorators.
Property Decorators.
Method Decorators.
Parameter Decorators
"""
print("1. example")

def make_pretty(func):

    def inner():
        print("i got decorated")
        func()
    return inner



@make_pretty
def ordinary():
    print("i got ordinary")

ordinary()

print("2.example")

def smart_devide(func):
    def inner(c,d):
        print("im going to devide", c ,"and", d)
        if d==0:
            print("whoops! cannot devide")
            return
        return func(c,d)
    return inner

@smart_devide
def devide(a,b):
    print(a/b)

devide(4,2)
devide(0,0)

print("3. example")

def upper_decor(fun):
    def wrapper():
        result=fun()
        return result.upper()
    return wrapper()

def hello_name():
    return "hello"

f=upper_decor(hello_name)
print(f)

print("3.example by adding decorator")

def upper_decor(fun):
    def wrapper(name):
        result=fun(name)
        return result.upper()
    return wrapper

@upper_decor
def hello_name(name):
    return  "hello" + name

print(hello_name(" arya"))






