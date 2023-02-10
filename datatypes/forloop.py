name="apple"
for i in name:
    print(i)

#range method

for x in range(1,11):
    print(x)

a= "python"
for i in a:
    print(i)

list=[1,2,3,4,5,6,7,8,9,10]
n=2
for i in list:
    c=n*i
    print(c)

print("sum of numbers 1 to 10")
list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list1:
    sum=sum + i
print("the sum is ",sum)

print("method 2 range method")
sum=0
for i in range(0,11):
    sum=sum+i
print(sum)
"""
sum of 1 to n numbers
"""
#n=int(input("enter the number : "))
#for i in range(1,n):
 #   n=n+1
#print(n)


"""even numbers from 1 to 10"""
print("even numbers from 1 to 10")
for i in range(0,11,2):
    print(i)

"""
multiplication table
"""
print("multiplication table")
a=int(input("enter the number: "))
for i in range(1,11):
    c=a*i
    print(a,"*",i,"=",c)


"""pattern printing"""
rows=int(input("enter the number of rows:"))
for i in range(0,rows+1): #rows
    for j in range(i): #column
        print("*",end =' ')
    print()


"""reverse pattern printing"""
rows=int(input("enter the number of rows: "))
for i in range(rows+1,0,-1):
    for j in range(i):
        print("*", end =" ")
    print()


"""pattern printing"""
n=int(input("enter the number of rows"))
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""pattern printing"""

n=int(input("enter the number of rows: "))
for i in range(0,n+1):
    for j in range(i):
        print(i,end=" ")
    print()