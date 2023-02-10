# 1. how to remove white space? strip method
# a="  python"
# b="     python   "
# print(a)
# print(b)
# print("strip method removes whitespace")
# print(a.strip())
# print(b.strip())

# swapcase
# a="environment"
# print(a.swapcase())

# join function
# a="apple"
# b="AB"
# c=a.join(b)
# print(c)

# break statement- terminates the currenly executing loop
# for i in range(10):
#     print(i)
#     if i==5:
#         break

# tuples
# immutable
# ordered
# allow duplicates
# indexed
# updations is not possible (immutable). if need to update need to change into another data type
# a=("apple",1,4,"banana")
# print(a)



# n=int(input("enter the series: "))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(2,n):
#     n3=n1+n2
#     print(n3)
#     n1,n2=n2,n3

# n=int(input("enter the number: "))
# if n==1:
#     print("not defined")
# for i in range(2,n+1):
#     f=0
#     if n%i==0:
#         f=f+1
# if f==2:
#     print("prime")
# else:
#     print("not prime")


x='pqrs'
for i in range(len(x)):
    x[i].upper()
print(x)


l1=[10,20,30,10,40,10]
print(l1.index(10))
x=[5,4,3,2,1]
x.extend(x)
print(x)

l=[1*x for  x in range(10,1,-4)]
print(l)

l=[2 * x for x in range(3,14,3)]
print(l)

count=1
def dothis():
    global count
    for i in(1,2,3):
        count+=1
dothis()
print(count)
