a={1:"apple",2:"banana"}
print(a)
a.update({3:"orange",4:"pineapple"})
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a.get(1))


# print("adding elements to a dictionary")
# d={}
# number=int(input("enter the number:"))
# for i in range(number):
#     key=int(input("enter the key"))
#     value=input("enter the value")
#     d.update({key:value})
# print(d)


"""functions"""

def sum():
    a,b=10,20
    s=a+b
    print("sum is: ",s)
sum()


def mul(a,b):
    m=a*b
    return m
m1=mul(5,10)
print("product is: ",m1)
print("prduct is: ",mul(10,20))

"""write a program to find factorial of a number with return type and function parameter"""

# n=int(input("enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial is: ",fact)

# """simple function"""
# def factorial():
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
#
#
# n=int(input("enter the number: "))
# factorial()
#
# """uding return value"""
# def factorial():
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
#
# n=int(input("enter the number: "))
# f1=factorial()
# print("factorial is: ",f1)
#
#
#
#
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
#
# print("factorial: ",10)
# f1=factorial(n)

# def student(st1,st2,st3):
#     print("first : ",st1)
#     print("second : ", st2)
#     print("third : ", st3)
#
# student(st2="anu",st3="arun",st1="kiran")
#
#
# print("all in 1")
# def student(x,*args,**kwargs):
#     print("simple argument",x)
#     for j in args:
#         print(j)
#     for i,j in kwargs.items():
#         print("%s=>%s"%(i,j))
#
#
# student("anju","anil","orange","apple",st1="anu",st2="arun",st3="kiran")

"""default parametr"""

def display(country="india"):
    print("iam from ",country)
display()
display("ekm")

"""list"""

def dis(ls):
    for i in ls:
        print(i)
dis([10,20,30])