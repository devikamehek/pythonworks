""" tuples .
immutable
ordered
allow duplicates
indexed
updations is not possible (immutable). if need to update need to change into another data type
"""
my_tuple=("apple","banana","orange",1,5,"apple")
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple[1])#positive indexing
print(my_tuple[-1])#negative indexing
print(my_tuple[1:3])#slicing
print(my_tuple[::-1])
print(my_tuple[:-1])
print(my_tuple[-3:-1])


print("2. list to tuple")
a=[1,2,3,"anj"]
print(a)
print(tuple(a))


print("3.multiple datatypes in tuples")
a=(1,2,["apple","orange"],{1:"a",2:"b"},"anj")
print(a)

print("4.nested tuple")
a=("apple","orange",("banana",1,2),5)
print(a)

print("5.updations in tuple :(updation in tuple is not possible,for "
      "that we will convert to mutable datatype and do the conversion")
a=(1,"apple","orange",5,6)
a=list(a)#convert to mutable datatype
a[0]="banana"
print(a)
a=tuple(a)#convert back to tuple
print(a)

print("6. append")
a=(1,2,"apple","banana","orange",4)
a=list(a) #convert to a list for appending
a.append("pineapple")
print(a)
a=tuple(a)#convert back to tuple
print(a)

print("7.adding tuple to a existing tuple")
a=("orange","pineapple")
b=("apple","banana")
a =a+ b
print(a)

print("8.Removing an item from tuple")
a=("orange","pineapple","apple","banana")
a=list(a)#convert to list for removing the item
a.remove("pineapple")#removing the item from list
print(a)
a=tuple(a)#convert back to tuple
print(a)

print("9. del method")
a=("orange","pineapple","apple","banana")
print(a)
del a
#a.clear()
# print(a) #error a is not defined
# print(a) #when deleting we will get error

print("10.Unpacking a tuple ")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)



print("11. for loop")
x=("apple","banana","cherry","orange")
for i in x:
  print(i)

a=("apple","banana","orange",1,3,2)
for i in range(1,len(a)):
    print(a[i])


print("12.while loop")
a=("apple","banana","cherry","orange")
i=0
while i < len(a):
    print(a[i])
    i=i+1


print("13. nested tuple")
n_tuple=("sikander",[8,4,6],(1,2,3))
print(n_tuple)
print(n_tuple[1]) #print the 1st index
n_tuple[1][1]=15 #changing element in the list[8,4,6]
print(n_tuple)
print(n_tuple[2][1])

print("changing sikander from the tuple n_tuple")
n_tuple=list(n_tuple) #convert to list
n_tuple[0]="apple"
print(n_tuple)
n_tuple=tuple(n_tuple)#convert back
print(n_tuple)

print("14. count method and index method")
my_tuple=('a','p','p','l','e',)
print(my_tuple.count(a))
print(my_tuple.index("p"))

print("15. existence of elements in tuple")
my_tuple=('a','p','p','l','e',)
print("a" in my_tuple)
print("f" in my_tuple)

