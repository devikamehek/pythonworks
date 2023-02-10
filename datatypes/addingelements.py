"""adding elements to a list using while loop"""
print("enter the number of elements adding to list:")
n=int(input())
print("enter" +str(n)+ "values to the list")
num=[]
i=1
while(i<=n):
    num.append(int(input()))
    i=i+1
print(num)