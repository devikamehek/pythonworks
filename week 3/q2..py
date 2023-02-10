"""write a python code to remove all the repeating letters from each words of a given sentence"""
# str1="lets google the pineapple"
# print("original string:",str1)
# remove_with_order="".join(set(str1))
# print("removed duplicates with order:",remove_with_order)
# remove_without_order="".join(set(str1))
# print("removed without order: ",remove_without_order)

str1="lets google the pineapple"
print("original string: ",str1)
str1=str1.split(" ")
# print(str1)
str2=[]
# print(str2)
for i in str1:
    # print(i)
    l=""
    for j in i:
        # print(j)
        if j in l:
            continue
        else:
            l=l+j
            # print(l)
    str2.append(l)
print("new string: "," ".join(str2))


print("method 2")
str1="lets google the pineapple"
str2=str1.split(" ")
# print(str2)
str3=""
str4=""
for i in str2:
    str3="".join(dict.fromkeys(i))
    str4=str4+str3+ " "
print(str4)


