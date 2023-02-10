# #num=int(input("enter the number:"))
# for i in range(num):#rows
#     for s in range(num-i-1):#spacing
#         print("",end=" ")
#     for j in range(i):#printing *
#         print("* ",end="")
#     print()

rows=int(input("enter the rows: "))
for i in range(0,rows+1):
    for s in range(rows-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()