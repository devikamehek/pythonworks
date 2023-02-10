"""largest of 3 numbers using nested if"""

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>c:
    print(b)
else:
    print(c)

# a=int(input("Enter A: "))
# b=int(input("Enter B: "))
# c=int(input("Enter C: "))
#
# # conditions to find largest
# if a>b:
#     if a>c:
#         g=a
#     else:
#         g=c
# else:
#     if b>c:
#         g=b
#     else:
#         g=c
#
# # print the largest number
# print("Greater  = ",g)