"""generate a python list all the even numbers between 4 and 30"""
"""using function"""
# def even():
#     a=[]
#     for i in range(start,stop):
#         if i % 2 == 0:
#             # print(i)
#             a.append(i)
#     print(a)
#
# start=int(input("enter the start value: "))
# stop=int(input("enter the stop value: "))
# even()




def even():
    l=[]
    for i in range(4,31):
       if i % 2 == 0:
           l.append(i)
    print(l)

print("Even numbers between 4 and 30")
even()








"""method 1"""
# for i in range(4,30,2):
#     print(i)

"""method 2"""
# start=int(input("enter the start value: "))
# stop=int(input("enter the stop value: "))
# a=[]
# for i in range(start,stop):
#     if i % 2==0:
#         # print(i)
#         a.append(i)
# print(a)