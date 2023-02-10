# # # # a=int(input("enter the first number:"))
# # # # b=int(input("enter the second number:"))
# # # # c=a+b
# # # # print(c)
# # #
# # # a="environment is pure"
# # # print(a.capitalize())
# # # print("is" in a)
# # # print(a.index("v"))
# # # print(a.find("v"))
# # # print(a.count("i"))
# # # print(len(a))
# # # print(a.isnumeric())
# # # print(a.split())
# # # print(a[::-1])
# # # print(a[1:5])
# #
# # # my_list=[1,2,3,4,5]
# # # print("the largest is:",max(my_list))
# #
# # # s=['p','y','t','h','o','n']
# # # s1=""
# # # print("combined string is:",s1.join(s))
# # #
# # #
# # # my_list=[1,2,3,4,5]
# # # total=1
# # # i=1
# # # while(i<len(my_list)):
# # #     print(my_list[i])
# # #     total=total*my_list[i]
# # #     i=i+1
# # # print("ans is:",t
# # #
# # # print("enter the number :")
# # # a=int(input())
# # # print("enter the elements to the list:")
# # # b=[]
# # # i=1
# # # while(i<=a):
# # #     b.append(int(input()))
# # #     i=i+1
# # # print(b)
# # #
# # # sum=0
# # # average=0
# # # i=0
# # # while(i<a):
# # #     sum=sum+b[i]
# # #     i=i+1
# # # average=sum/a
# # # print(average)
# #
# # a=int(input("enter the number: "))
# # b=a*a
# # print("square is",b)
#
# maximum=int(input("enter the maximum value: "))
# number=1
# total=0
# while(number<maximum):
#     if(number%2==0):
#         total=total+number
#     print(number)
#
#

maximum=int(input("enter the maximum value: "))
total=0
num=1
while(num<maximum):
    if(num%2==0):
        print(num)
        total=total+num
    num=num+1
print(num)