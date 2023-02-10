"""remove empty string from a list of strings"""
str1=["john"," ","jack","emma"," ","jins","lina"]
print("the original str1: ",str1)
while(" " in str1):
    str1.remove(" ")
print("The modified string is: ",str1)

