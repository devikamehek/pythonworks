print("1.write a python program to convert a string into a tuple")
a="apple"
print(a)
a=tuple(a)
print(a)

print("2.write a python program to convert a list into a tuple")
a=[1,2,3,"apple","banana","orange"]
print(a)
a=tuple(a)
print(a)

print("3. write a python program to print repeated items from a tuple")
a=(1,2,3,1,3,3,4,5,4,4,6,4,3)
print("tuple :",a)
b=int(input("enter the number:"))
count=a.count(int(b))
print("the count is:",count)

print("method 2")
a=(1,2,3,1,3,3,4,5,4,4,6,4,3)
print("Tuple is : ",a)
b=set()
for i in a:
    if a.count(i)>1:
        b.add(i)
print(f'Repeated elements in tuple {tuple(b)}')


