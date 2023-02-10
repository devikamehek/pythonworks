"""
how wold you check if each word in a string begins with a capital letter
answer : we use title() function
"""
str="Environment is beautiful"
print(str.istitle())

str1="Hi This "
print(str1.istitle())

"""
check if string contains a specific substring
answer: in operator
"""
a="this is a car"
print("is" in a)
print("for" in a)

"""
find the index of first occurence of a substring in a string
answer:index () , find() function
"""

a="malayalam is a language"
print(a.find("is"))
print(a.index("a"))

"""
count the total number of characters in a string
answer:len()
"""

a="english is a good languages in the world"
print(len(a))

"""
count the number of specific character in a string
answer: count()
"""
a="malayalam is a language in india"
print(a.count("a"))

"""
capitalise the first character of the string
answer: capitalize()
"""

a="environment is pure"
print(a.capitalize())

"""
check if string contains only numbers
answer:isnumeric()
"""
a="environment"
print(a.isnumeric())
b="6000"
print(b.isnumeric())

"""
split the string on a specific character
answer:split()
"""
print("split method")
str="environment is the purest"
print(str.split())

"""
reverse the string 
answer:string splicing [::-1]
"""

a="Hello hai"
print(a[::-1])

"""
join a list of strings into a single string,delimited by hyphens. hint: (.join() function)
"""
a=["hi","this","is","a","car"]
b="-".join(a)
print(b)

a="hi"
b="hello"
print("-".join([a,b]))
"""
give an example of string slicing
"""
a="environment"
print(a[1:5])
print(a[-1])

"""
convert an integer into a string
answer:str() function
"""
a="7"
print(a)


"""
replace all instances of substring in a string
answer:replace()
"""
a="color is red"
b=a.replace('red','blue')
print(b)
print(a.replace('o','f',2))

"""
remove whitespace from left,right or both sides of a string
answer:strip()
"""
a="   environment is purity "
print(a.strip())
print(a)
print(a.rstrip())
print(a.lstrip())

"""
what does it mean for string to be immutable in python
answer:once a string object is created it cannot be changed. modyfying it creates a whole new string.
"""

