"""get only unique elements from 2 sets"""

a={1,2,3,5,6,6,6}
b={2,3,4,6,3,1,5,4}
print("The unique elemets are: ",a|b)
print("unique elements in set a is: ",set(a))
print("unique elements in set b is: ",set(b))
print("unique elemets in a and b is: ",a.union(b))