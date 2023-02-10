"""if we do not know the errors, there is a built in class called exception"""
try:
    n1=int(input("Enter A: "))
    n2=int(input("Enter B: "))
    n3=n1/n2
    print("Output is: ",n3)

except Exception as ex:
    print(ex)

"""if we know the errors we will do this"""

try:
    n1=int(input("Enter A: "))
    n2=int(input("Enter B: "))
    n3=n1/n2
    print("Output is: ",n3)
except ZeroDivisionError as er:
    print(er)
except ValueError as er:
    print(er)

