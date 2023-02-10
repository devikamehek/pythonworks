"""calculate the number of uppercase and lowercase in a string"""
a="EnvironMENT is Pure"
upper=0
lower=0
for i in range(len(a)):
    if a[i].isupper():
        upper += 1
    else:
        a[i].islower()
        lower += 1
print("The string is: ",a)
print("Upper case: ",upper)
print("Lower case: ",lower)
