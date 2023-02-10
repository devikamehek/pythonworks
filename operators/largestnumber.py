a = int(input("Enter a value to a "))
b = int(input("Enter a value to b "))
c = int(input("enter a value to c "))
if a >= b and a >= c:
    print("a is greater than b and c")
elif b >= a and b >= c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")
