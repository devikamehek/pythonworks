#a = 3
#b = 5
#c =int (input("enter a number"))
#if b > a:
 #   print("b is greater than a")
#elif a == b:
 #   print("equal")
#elif b < a:
 #   print("a is less than b")
#else :
 #   print("false")


a =int(input("enter a number to a"))
b =int(input("enter a number to b"))
c =int(input("enter a number to c"))
if (a<b and b>c):
    print("b is greater than a and b")
elif (a<b or b<c):
    print("b is greater")
else:
    print("invalid")
