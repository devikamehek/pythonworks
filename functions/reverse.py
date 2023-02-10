"""write a python program to  reverse a string using function"""



def reverse_string(string1):
    string1=string1[::-1]
    return string1

a=" 1234abcd"
print("The original string is :",a)
print("The reversed string is: ",reverse_string(a))











"""method 2"""
# a="environment"
# print("The string is:",a)
# print("The reverse is: ",a[::-1])

"""method 3"""
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# s = "environment"
# print("The original string is : ",s)
# print("The reversed string(using loops) is : ",reverse(s))
