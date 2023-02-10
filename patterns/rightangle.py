print("right angle")
row=int(input("enter the number of rows: "))
for i in range(0,row+1):#rows
    #print(i)
    for j in range(i):#colums
        print("* ",end=" ")
    print()

print("inverted right angle")
row=int(input("enter the number of rows: "))
for i in range(0,row+1):#rows
    for j in range(row-i):
        print("* ",end=" ")
    print()

print("with numbers")
row=int(input("enter the number of rows: "))
for i in range(0,row+1):#rows
    #print(i)
    for j in range(i):#colums
        print(i,end=" ")
    print()

