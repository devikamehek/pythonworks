def add(a,b):
    print("Answer is: ",a+b)
def sub(a,b):
    print("Answer is: ", a - b)
def mul(a,b):
    print("Answer is: ", a * b)
def div(a,b):
    print("Answer is: ", a / b)

print("Calculator")
num1=int(input("Enter the First Number: "))
num2=int(input("Enter the Second Number: "))
op=int(input("1 for Addition\n2 for substraction\n3 for multiplication\n4 for division\nChoose your option: "))

if op==1:
    add(num1,num2)
elif op==2:
    sub(num1,num2)
elif op==3:
    mul(num1,num2)
elif op==4:
    div(num1,num2)
else:
    print("invalid choice")

# print("calculator")
# num1=int(input("enter num1: "))
# num2=int(input("enter num2: "))
# choice=int(input("1.addition\n2.sub\n3.div\n4.mul\n Enter your choice: "))
# if choice==1:
#     print("sum is: ",num1+num2)
# elif choice==2:
#     print("diffrence is: ",num1-num2)
# elif choice==3:
#     print("remainder is: ",num1/num2)
# elif choice==4:
#     print("multiply is: ",num1*num2)
# else:
#     print("invalid choice")




