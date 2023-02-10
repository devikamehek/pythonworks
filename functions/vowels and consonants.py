"""Define a function which counts vowels and consonant in a word"""
def count(val):
    vowels=0
    consonents=0
    y=["a","e","i","o","u"]
    for i in range(len(val)):
        if val[i] in y:
            vowels=vowels+1
        else:
            consonents=consonents+1
    print("The Count of Vowels is: ",vowels)
    print("The count of consonents is: ",consonents)

x=input("Enter a String: ")
count(x)
