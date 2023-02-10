"""
all(),any(),enumerate(),len(),max(),min(),sorted(),sum(),tuple()
"""
print("1. all() function")
my_tuple=("apple","banana","orange",1,5,"apple")
print(all("apple"))
print(all("cherry"))

print("2. any() function")
my_tuple=("apple","banana","orange",1,5,"apple")
print(any("apple"))
print(any("k"))

print("3. len() function")
my_tuple=("apple","banana","orange",1,5,"apple")
print(len(my_tuple))

print("4. max() function and min() function")
print(max(1,5))
print(min(1,5))

print("5. sum and sorted functions")
b=1,2,4,5,6,8,7,9
print(sum(b))
print(sorted(b))

print("6. enumerate fun")
a=("apple","orange","banana")
b=enumerate(a)
print(tuple(b))

names=["messi","Depaul","neimer"]
age=[24,25,27]
for i,(names,age) in enumerate(zip(names,age)):
    print(i,names,age)

print("2.")
name=("apple","banana","orange")
age=(23,54,65)
for i,(name,age) in enumerate(zip(name,age)):
    print(i,name,age)

print("3.")
name=("a","b","c","d","e")
# b=enumerate(name)
# print(tuple(b))
for i,name in enumerate(name):
    print(i,name)



print("4.")
letters=[("a","A"),("b","B")]
for i,letters in enumerate(letters):
    #print(i,letters)
    print("Letter %d is %s/%s" %(i,letters[0],letters[1]))


print("7. zip function")
name=("apple","banana","orange")
age=(23,54,65)
for i,(name,age) in enumerate(zip(name,age)):
    print(i,name,age)

print("8. map function")
l=("app","car","ice","mat")
#map() can listify the list of strings individually
test=tuple(map(tuple,l))
print(test)

