#normal function
def sum(a,b):
    return a+b
print(sum(2,3))


#lamda function
#syntax- lamda arguments:expression
add=lambda a,b: a+b
print(add(2,3))

mul=lambda a,b,c: a*b*c
print(mul(2,3,4))


largest=lambda a,b:a if a>b  else b
print(largest(2,3))

#filter
l=[10,2,3,4,50,77,11,12]
lst=list(filter(lambda x:x%2==0,l))
print(lst)

#map
l=[10,2,3,4,50,77,11,12]
lst=list(map(lambda x:x*2,l))
print(lst)

#reduce
from functools import reduce
l1=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,l1)
print(product)

