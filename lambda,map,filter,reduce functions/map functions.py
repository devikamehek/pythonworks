"""The map() function executes a specified function for
 each item in an iterable. The item is sent to the function as a parameter."""

"""syntax: map(function, iterables)"""

def myfunc(a):
  return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convert the map into a list, for readability:
print(list(x))


def my_fun(a,b):
    return a+b

x=map(my_fun,("apple","orange","banana"),("A","B","C"))
print(list(x))
