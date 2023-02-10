# # a="apple"
# # print(a)
# # print(a[4])
# # print(len(a))
#
# # a="banana"
# # for i in a:
# #     print(i)
# #
# #
# # a="banana"
# # print(len(a))
# # i=0
# # while i<len(a):
# #     letter=a[i]
# #     print (i,letter)
# #     i=i+1
#
# a="EnvironMENT is Pure"
# upper=0
# lower=0
# for i in range(len(a)):
#     if a[i].isupper():
#         upper += 1
#     else:
#         a[i].islower()
#         lower += 1
# print("The string is: ",a)
# # print("upper case is: ",upper)
# # print("lower case is: ",lower)
#
#
# # str="Environment is beautiful"
# # print(str.istitle())
# #
# # a=["hi","this","is","a","car"]
# # a="-".join(a)
# # print(a)
#
# # list=[1,4,7,8]
# # print(list[1])
#
# my_list=[1,2,3,4,5]
# i=0
# sum=0
# while i<len(my_list):
#     sum=sum+my_list[i]
#     i=i+1
# print(sum)
#
# my_list=[1,2,-8,0]
# print(max(my_list))
#
# s=['p','y','t','h','o','n']
# s1=""
# print(s1.join(s))
#
#
# my_list=[1,2,3,4,5]
# i=1
# sum=1
# while i<len(my_list):
#     sum=sum*my_list[i]
#     i=i+1
# print(sum)
#
#
# str1="python"
# for i in str1:
#     print(i)
#
# for i in range(10):
#     print(i,end=" ")
#
# n=int(input("enter the number: "))
# i=1
# while i<=10:
#     print("%d X %d = %d"%(n,i,n*i))
#     i=i+1

# n=int(input("enter the rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# n=int(input("enter the rows: "))
# for i in range(n+1):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# n=int(input("enter the rows: "))
# for i in range(0,n+1):
#     for s in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" * ",end=" ")
#     print()

# n=int(input("enter the rows: "))
# for i in range(0,n+1):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(" * ",end=" ")
#     print()

# n=int(input("enter the rows: "))
# for i in range(0,n+1):
#     for j in range(i):
#         print("* ",end=" ")
#     print()

# n=int(input("enter the rows: "))
# for i in range(0,n+1):
#     for s in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" * ",end=" ")
#     print()
# for i in range(0,n+1):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(" * ",end=" ")
#     print()
#
#
# n=int(input("enter the total number of elements to enter: "))
# print("enter the "+str(n)+ " elements to the list")
# List=[]
# i=1
# while i<=n:
#     List.append(int(input()))
#     i=i+1
# # print(List)
#
# average=0
# sum=1
# while(i<n):
#     sum =sum+ List[i]
#     i=i+1
# average=sum/n
# print(average)

#
# n=int(input("enter the number: "))
# rev_num=0
# i=0
# while i<n:
#     remainder=n%10
#     rev_num=(rev_num*10)+remainder
#     n=n//10
# print("reverse number: ",rev_num)

# n=int(input("enter the value:"))
# n1=0
# n2=1
# sum=0
# while(n1<=n):
#     sum=n1+n2
#     n1=n2
#     n2=sum
#     print(n1)

n=int(input("enter the limit: "))
even=[]
odd=[]
i=0
while i<=n:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even:",even)
print("odd: ",odd)
