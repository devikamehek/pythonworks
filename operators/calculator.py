def add(x, y):
    return x + y
def sub(x,y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y



print("select an option")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

while True:
    choice=input("Enter your choice 1,2,3,4")
    if choice in ('1','2','3','4'):
        num1=float(input("Enter the first number"))
        num2=float(input("Enter the second number"))

        if choice=='1':
            print(num1, "+", num2,"=" , add(num1,num2))

        elif choice=='2':
            print(num1, "-", num2, "=" ,sub(num1,num2))

        elif choice=='3':
            print(num1, "*", num2, "=" ,mul(num1,num2))

        elif choice=='4':
            print(num1,"/", num2, "=", div(num1,num2))

    nextcalc= input("can we exit ? (yes/no)")
    if nextcalc == "yes":
        break

    else:
        print ("exit")



# print("calculator")
# print("enter your choice: ")
# print("1. addition,2. multiplication,3. division,4. substraction")
# ch=int(input("enter your choice: 1,2,3,4: "))
# n1=int(input("enter the n1: "))
# n2=int(input("enter the n2: "))
# if ch==1:
#     print("result is: ",n1+n2)
# elif ch==2:
#     print("result is: ",n1*n2)
# elif ch==3:
#     print("result is: ",n1/n2)
# elif ch==4:
#     print("result is: ",n1-n2)
# else:
#     print("invalid choice")