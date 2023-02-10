"""method 1"""
print("method 1- using math.gcd function")
import math
num1=int(input("enter the first number:"))
num2=int(input("enter the second number: "))
print(f'The GCD of {num1} and {num2} is ',math.gcd(num1,num2))


"""method 2 """
print("method 2")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
gcd=1
for i in range(1,min(num1,num2)):
    if(num1%i==0) and (num2%i==0):
        gcd=i
print(f'GCD of {num1} and {num2} is,',gcd)

