"""
unique elements
unordered
immutable
unindexed
mathematical operations are possible:union,intersection etc
duplicates not allowed in sets

set items are unchangable,but we can add and remove items.
"""
print("1.set()")
set1={1,2,3,"apple",(4,5,6)}
print(set1)

print("2. Empty set")
set1=set()
print(set1)

# print("3.we cannot print a mutable datatype like set inside a set. for that we need to change the list to set")
# set1={1,2,3,"apple",[1,2,3]}
# #print(set1) #error will come

print("4. List in set()")
set1=([1,2,3])
print(set(set1))
print(type(set1))

a=set([1,2,4])
print(a)
print(type(a))

print("5. accesing elements from set- union,intersection,difference,symmetric difference")
A={1,2,3,4,5}
B={4,5,6,7,8}
print("Union of the set is: ",A|B)
print("intersection of the set is: ",A&B)
print("difference of the set is: ",A-B)
print("symmetric difference of the set is: ",A^B)


