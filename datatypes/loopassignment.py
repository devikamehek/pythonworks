print("answer 1.")
n=int(input("enter the number of rows: "))
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("answer 2.")
n=int(input("enter the number of rows: "))
for i in range(n+1,1,-1):
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

print("full pyramid pattern printing")
n=int(input("enter the number of rows:"))
for i in range(n): #rows
    for s in range(n-i-1): #space
        print(" ", end="")
    for j in range(i+1): #column * printing
        print("* ",end="")
    print()


"""create a diamond pattern"""
n=int(input("enter the number of rows: "))
for i in range(n):
    for s in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(n):
    for s in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()


