""" check if all items in a tuple are same"""
#
# List = ['Mon','Mon','Mon','Mon']
# # Using all()method
# result = all(element == List[0] for element in List)
# if (result):
#    print("All the elements are Equal")
# else:
#    print("All Elements are not equal")

x = (True, True, True)
result = all(x)
print(result)

x = (True, True, False)
result = all(x)
print(result)

print("method 1:")
tup=(1,1,1,1,1)
f=1
for i in tup:
    for j in range(i,len(tup)-1):
        if tup[i]!=tup[j+1]:
            f=0
            break
if f==1:
    print("same")
else:
    print("not same")

print("method 2:")
tup=(1,1,1,1,1,5,6)
tup=set(tup)
if len(tup)==1:
    print("same")
else:
    print("not same")






