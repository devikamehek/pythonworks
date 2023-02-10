"""1."""
print("1. to access the value 20 from tuple")
tple=(1,2,40,30,20)
print(tple[4])

tple1=(1,2,40,[10,2,39],930,20,10)
print(tple1[5])

print("remove repeated items from tple: method 1")
tple=(1,2,40,30,20,40)
print("given tuple is :",tple)
t=tuple(set(tple)) #convert to set
print(t)


print("remove repeated items from tple: method 2")
tple=(1,2,40,30,20,40)
print("given tuple is :",tple)
a=[]
for i in tple:
    if i not in a:
        a.append(i)
tple=tuple(a)
print(a)










