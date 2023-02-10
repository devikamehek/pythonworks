"""2.Write a Python
function to create and print a list where
the values are square of numbers between 1 and 30 (both included)."""
def square():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    print(l)

print("The square of Numbers between 1 and 30: ")
square()
