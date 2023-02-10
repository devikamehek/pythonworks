print("inverted pyramid")
rows=int(input("enter the rows: "))
for i in range(0,rows+1):
    for s in range(i):
        print(" ",end=" ")
    for j in range(rows-i):
        print("* ",end=" ")
    print()