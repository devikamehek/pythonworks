# a=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750}]
# print("The given dictionary is :",a)
# newdict={}
# list1=[]
# for d in a: #d gives each dictionary
#     p=list(d.values()) #create list of values
#     list1.append(p[0])
#     list1.append(p[1])#list contains all individual values in a single list
# #print(list1)
# for i in range(0,len(list1),2): #taking each 2nd item in the list1
#     if list1[i] in newdict:
#         rep=list1[i]
#         index=list1.index(rep) #finding index of repeated variable
#         list1[index+1]=list1[index+1]+list1[i+1] #adding corresponding
#         newdict[list1[i]]=list1[index+1] #updating value of repeated
#     else:
#         newdict.setdefault(list1[i],list1[i+1]) #adding values to dictionary
# print("The combined dictionary is",newdict)

SampleData=[{"item":"item1","amount":400},
            {"item":"item2","amount":300},
            {"item":"item1","amount":750}]
print(SampleData)
itemdict={}
for i in SampleData:
    a=list(i.values())
    #print(a)
    print(f'a={a}')
    if a[0] not in itemdict:
        itemdict[a[0]]=a[1]
    else:
        v=itemdict[a[0]]
        itemdict[a[0]]=v+a[1]
print(itemdict)

"""method 2"""
print("mrthod 2")
d=[{"item":"item1","amount":400},
    {"item":"item2","amount":300},
    {"item":"item1","amount":750}]
lst={}
for i in d:
    if i["item"] not in lst:
        lst[i["item"]]=i["amount"]
    else:
        lst[i["item"]]=lst[i["item"]]+i["amount"]
print(lst)
