"""remove items from set1 that are not common to both set1 and set2"""

set1={"apple","banana",1,3,2,4,5,6}
set2={"apple",1,3,2,4,3,8,9,0}
print("The total elements in set1 and set2:",set1|set2)
print("common elements: ",set1&set2)


print("method 2")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)