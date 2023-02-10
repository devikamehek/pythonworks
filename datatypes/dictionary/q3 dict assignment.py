"""dictionary from a string"""
str1="Luminar"
print("The given string is :",str1)
dict1={}
for i in range(1,len(str1)+1):
    dict1.setdefault(i,str1[i-1])
    #print(i,str1[i-1])
print("The corresponding dictionary is:",dict1)

