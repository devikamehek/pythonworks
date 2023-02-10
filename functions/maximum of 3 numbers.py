"""write a python program to find the maximum of 3 numbers"""
def maximum():
    if(a>b and a>c):
        print(str(a)," is greater than", str(b),"and ",str(c))
    elif(b>a and b>c):
        print(str(b)," is greater than", str(a),"and ",str(c))
    else:
        print(str(c)," is greater than", str(a),"and ",str(b))

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
maximum()





# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# c=int(input("Enter c: "))
# if(a>b and a>c):
#     print(str(a)," is grater")
# elif(b>a and b>c):
#     print(str(b), " is grater")
# else:
#     print(str(c), " is grater")

