"""program to print 1 to 10"""
print("while loop")
i=1
while(i<=5):
    print(i)
    i=i+1

print("for loop")
for i in range(0,6):
    print(i)

""" program to print multiplication table"""
i=1
number=int(input("enter the  number :"))
while(i<=10):
    print("%d * %d =%d"%(number,i,number*i))
    i=i+1
