print("half pyramid with numbers")
n=int(input("enter the number: "))
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("half inverted pyramid with reverse number")
n=int(input("enter the number:"))
for i in range(0,n+1):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()
