print("1. normal method")
fruits=["apple","banana","pineapple","orange"]
new_list=[]
for x in fruits:
    if "a" in x:
        new_list.append(x)
print(new_list)

"""List comprehension syntax: newlist = [expression for item in iterable if condition == True]"""
"""List comprehension offers a shorter syntax when you want to create a
 new list based on the values of an existing list"""

print("2.Using list comprehension")
fruits=["apple","banana","pineapple","orange"]
new_list=[x for x in fruits if "a" in x]
print(new_list)


print("3. new example")
"""list comprehension"""
newlist = [x for x in range(10) if x < 5]
print(newlist)

"""normal method"""
new=[]
for i in range(10):
    if i <5:
        new.append(i)
print(new)

print("4. Multiple conditions")
new_list1=[x for x in range(100) if x%2==0 if x%5==0 if x%3==0]
print(new_list1)

print("5. multiple loops")
prime=[x for x in range(2,21) if all(x%y!=0 for y in range(2,x))]
print(prime)

print("6.")

h_letters=[]
for letter in "human":
    h_letters.append(letter)
print(h_letters)


h_letters=[letter for letter in "human"]
print(h_letters)

print("7.even and odd list")
even_odd=[x for x in range(100) if x%2==0]
odd_even=[x for x in range(100) if x%2!=0]
print(even_odd)
print(odd_even)

print("8.sum of n natural numbers")
natural_numbers=sum([x for x in range(1,int(input("enter the range: "))+1) if x])
print(natural_numbers)

natural_numbers=sum([x for x in range(11)])
print(natural_numbers)

natural_numbers=[(n*(n+1)/2) for n in range(11)]
print(natural_numbers)

