"""sum of natural numbers using recursion"""

"""recursion: a function calling itself multiple times is called recursion"""

def getsum(num):
    if num==1:
        return 1
    return num + getsum(num-1)

num=int(input("enter num: "))
print("The sum is: ",(getsum(num)))


