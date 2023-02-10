for i in [10,20,30]:#list,string,tuple etc
    print(i)

# for i in range(start,stop,step):

# """To print fibanocci series with range method"""
# print("fibanocci series")
# n=int(input("enter the number of series: "))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(2,n):
#     n3=n1+n2
#     print(n3)
#     n1,n2=n2,n3
#
#
# print("prime number")
# n=int(input("enter the range: "))
# #n=5----5%1=0,5%2=1,5%3=2,5%4=3,5%5=0
# f=0
# if n==1:
#     print("not defined")
#
# for i in range(1,n+1):
#     if n%i==0:
#         f=f+1 #2
#
# if f==2:
#     print("prime")
# else:
#     print("not prime")


print("else stetement in for runs after completing full for loop")
for i in "python":
    print(i)
else:
    print("completed")

print("break statement")
l=[10,20,30,40,50,100,35,45]
for i in l:
    # print(i)
    if i==100:
        break
    print(i)

print("continue statement")
l=[10,20,30,40,50,100,35,45]
for i in l:
    # print(i)
    if i==100:
        continue
    print(i)

print("sorting")
l=[10,34,56,23,43,2000,36,562]
l.sort()
print(l)
print("reverse sorting")
l=[10,34,56,23,43,2000,36,562]
l.sort(reverse=True)
print(l)

print("1.adding elements to list")
n=int(input("enter the number to be appended to list: "))
print("enter"+str(n)+"elements to list")
l=[]
for i in range(1,n+1):
    l.append(int(input()))
print(l)