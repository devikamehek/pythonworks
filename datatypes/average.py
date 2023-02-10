"""find the average to 5 numbers using while loop"""
print("enter the value of n: ")
n=int(input())
print("enter"+str(n)+ "numbers")
num=[]
i=0
while(i<n):
    num.append(int(input()))
    i=i+1

sum=0
i=0
average=0
while(i<n):
    sum=sum+num[i]
    i=i+1
average=sum/n
print("the average is:",average)
