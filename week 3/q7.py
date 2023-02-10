"""write a program for python function that takes a list of words and
returns the lenght of the longest one"""

a=["php","java","python","c++"]
print("List is: ",a)
max1=max(a)
print("longest word is: ",max1)
print("Lenght of the longest word is:",len(max1))


print("2")
list2=["hi","hello","welcome","environment"]
print("List is:",list2)
max1=len(list2[0])
temp=list2[0]
for i in list2:
    if(len(i)>max1):
        max1=len(i)
        temp=i
print("Longest word is: ",temp)
print("Length of the Longest word is: ",len(temp))
