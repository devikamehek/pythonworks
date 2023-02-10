"""check if two sets have any common elements. if yes display the common elements"""
print("q1.")
a={1,2,3,5,6,6,6,"apple","banana","a"}
b={2,3,4,6,3,1,5,"banana"}
print("The common elements are: ",a&b)


print("q2.")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))


print("method 2")
set1={10,20,30,40,50}
set2={30,40,50,60,70}
print("common elemets are: ",set1&set2)
