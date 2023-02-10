"""write a python program to find the sum of all numbers in a list using function"""
# a=[1,2,3,4,5]
# sum=0
# print("List is: ",a)
# for i in a:
#     sum=sum+i
# print("sum is: ",sum)

def sum(a):
    add=0
    for i in a:
        add=add+i
    print("sum is: ",add)
a = [1, 2, 3, 4, 5]
sum(a)

"""write a python program to multiply all elements in a list using function"""

def multiply(a):
    mul=1
    for i in a:
        mul=mul*i
    print("multiply is: ",mul)
a = [1, 2, 3, 4, 5]
multiply(a)













"""square of a given number"""
def square(num):
    print("square is: ",num*num)
a=int(input("enter the number: "))
square(a)
