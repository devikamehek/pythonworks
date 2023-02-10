a="environment"
print(a[4]) #string indexing

print(a[1:4])
print(a[-1])
print(a[:-1])
print(a[::-1])

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.count("e"))
print(a.isalpha())
print(a.isalnum())
print(a[2:5])

#concatenation

str1 = "hello"
str2 = "hi"
new_str = str1 + str2
print(new_str)

st1 = "hi"
st2 = "6"
new_st =st1 + st2
print(new_st)

str1 ="hiiii"
str2 = 8
new_str = str1 + " " + str(str2)
print(new_str)

#len function

fruit="banana"
print(len(fruit))

#looping- for loop and while loop

fruit="banana"
index=0
while index<len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index+1


color="black"
index=0 #initialisation
while index<len(color): #condition checking
    letter=color[index]
    print(letter,index)
    index=index+1

#for loop
fruit="banana"
for i in fruit:
    print(i)

#find function
fruit="apple"
ans=fruit.find('le')
print(ans)

#replace function

x="apple banana"
y=x.replace('banana','mon')
print(y)

x="apple banana"
print(x.replace('a','f'))
print(x[:2].replace("p",'t'))
print(x[3])

#string formatting

name='peter'
age=23
print('%s is %d years old' %  (name,age))
print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')

bags=5
apples_in_bag=12
print(f'There are {bags*apples_in_bag} apples in the bag')


val1=5
val2=8
print(f'The sum is {val1+val2}')
print('The sum is {} * {}'.format(val1,val2))

a="apple"
b=3
c=4
d='bananas'
print('I have %d %s and %d %s' %(b,a,c,d))
print(f'I have {b,a} and {c,d}')

"""
replace each symbol with #
conditional 
"""
a="/*jon is @developer & musician!!"
print(a.replace('/','#').replace('*','#').replace('@','#').replace('&','#').replace('!','#'))

a="/*jon is @developer & musician!!"
if("*,/,@,&,!" in a):
    print(a.replace("*,/,@,&,!","#"))

else:
    print("no symbols ",a)



"""
append new string in the middle of a given string
s1="Luminar"
s2="python"
o/p="LumiPythoninar"
"""

s1="Luminar"
s2="python"
p=s1[0:4]
q=s1[3:7]
print(p +s2 +q)


s1="Luminar"
s2="python"
length_of_s1=len(s1)
middle_of_s1=length_of_s1//2
s3=s1[0:middle_of_s1+1]
s4=s1[middle_of_s1:length_of_s1]
print(s3+s2+s4)