""" write a program to get a string from a given string where all the occurences of its first char
 have been changed to "$",except the first char itself.
 sample o/p: 'restart'
 o/p:'resta$t'
 """

str1="restart"
print("string is :",str1)
char=str1[0]
# lenght=len(str1)
str1=str1.replace(char,"$")
str1=char+str1[1:]
print(str1)


