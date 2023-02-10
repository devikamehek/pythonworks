"""
1. sum of all items in a list
my_list=[1,2,3,4,5]
"""
print("1.")
my_list=[1,2,3,4,5]
total=0
ele=0
while(ele < len(my_list)):
    total= total + my_list[ele]
    ele = ele + 1
print("sum is ",total)

"""
2.write a python program to get the largest number from a list
List1=[1,2,-8,0]
"""

print("2.")
list1=[1,2,-8,0]
print("first method: the largest number is",max(list1))
list1.sort()
print("second method: the largest number is ",list1[-1])


"""
3.write a python program to convert a list of characters into a string
s=['p','y','t','h','o','n']
"""
print("3.")
s=['p','y','t','h','o','n']
s1=""
print(f'the combined value is {s1.join(s)}')


"""
4. write a python program to multiply all items in a list
"""
print("4.")
my_list=[1,2,3,4,5]
total=1
element=0
while(element < len(my_list)):
    total = total * my_list[element]
    element = element + 1
print("multiplication answer is",total)

