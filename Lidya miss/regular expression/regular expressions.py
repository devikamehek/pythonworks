#findall()
print("1.findall() method")
import re
str1="rose is a beautiful and colorfull flower"
s=re.findall("ful",str1)
print(s)

s1=re.findall("are",str1)
print(s1)

d="cat mat pat rat sat"
a=re.findall("[scr]",d)
print(a)
b=re.findall("[scr]at",d)
print(b)


print("2.^-start with")
d="cat mat rat pat sat"
a=re.findall("[^scr]",d)
print(a)

print("3.\d- read only digits")
d="cat rat mat pat sat 99900 9998 9798 3649 745"
a=re.findall("\d{4}",d)
print(a)
b=re.findall("\d{1,3}",d)
print(b)

print("4.r \ b -space")
d="cat rat mat pat sat 99900 9998 9798 3649 745"
a=re.findall(r"\b\d{3}\b",d)
print(a)

#search()
print("5. search() method")
print("5.\s- white space")
str1="class will start at 10am"
s=re.search("\s",str1)
print(s)
print(s.start())

print("7.\d-digits")
s1=re.search("\d",str1)
print(s1.start())

s2=re.search("python",str1)
print(s2)

print("8.^-start with,.-any characters,*-,$-end with")
str2="class will start at 10am"
s=re.search("^class.*10am$",str2)
print(s)
if s:
    print("find")
else:
    print("not find")


#split() method
print("9. split() method")
str1="class will start at 10am"
s=re.split(" ",str1)
print(s)
s1=re.split("a",str1)
print(s1)
s2=re.split(" ",str1,2)
print(s2)

print("10. fullmatch()  method")
str2="versions are python1 python2"
a=re.fullmatch(str2,"versions are python1 python2")
print(a)


print("11. sub() method")
str3="rose and jasmine are flowers"
a=re.sub(' ','*',str3)
print(a)

b=re.sub(" ","*",str3,3)
print(b)
