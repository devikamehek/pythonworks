"""It provides an easy way to apply operations on a list.
it creates a new list in which each element is the result of applying a given operation in a list"""

l=[x+3 for x in [1,2,3]]
print(l)

a=[x for x in range(10) if x>5]
print(a)

x=[x for x in range(26) if x%2==0]
print(x)

v=["a","e","i","o","u"]
x=[a for a in "environment is pure" if a in v]
print(x)

str1="hai how are you"
words=str1.split( )
print(words)
firstletter=[i[0] for i in words]
print(firstletter)


colors=["red","white","green","pink"]
a=[x for x in colors if 'e' in x]
print(a)

colors=["red","white","green","pink"]
b=[x for x in colors if x!="green"]
print(b)

colors=["red","white","green","pink"]
b=[x if x!="green" else "blue" for x in colors]
print(b)
