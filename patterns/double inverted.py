num=int(input("enter the number:"))
for i in range(num):#rows
    for s in range(i):#spacing
        print(" ",end="")
    for j in range(num-i):
        print("* ",end="")
    print()
for i in range(num-1,-1,-1):#rows
    for s in range(i):#spacing
        print(" ",end="")
    for j in range(num-i):
        print("* ",end="")
    print()

print("type 2")
#num=int(input("enter the number:"))
for i in range(num):#rows
    for s in range(i):#spacing
        print(" ",end="")
    for j in range(num-i):
        print("* ",end="")
    print()
for i in range(num):
    for s in range(num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
