choice = input("enter the choice  : +,-,*,/: ")
a = int(input("enter a number to a: "))
b = int(input("enter a number to b: "))
if choice== '+':
    print("sum is ", a+b)
elif choice== '-':
    print("difference is", a-b)
elif choice== '*':
    print("multiply is", a*b)
elif choice== '/':
    print("div is", a/b )
else:
    print("invalid")
