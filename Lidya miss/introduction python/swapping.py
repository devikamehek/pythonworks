# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)

a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
print("before swapping ")
print("a= ",a)
print("b= ",b)
print("after swapping")
a,b=b,a #swapping
print("a= ",a)
print("b= ",b)