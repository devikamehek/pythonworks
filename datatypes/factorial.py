"""factorial using for loop"""


print("for loop")
n=int(input("enter the number: "))
i=1
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("Factorial: ",factorial)




"""factorial using while loop"""
print("while loop")
n=int(input("enter the number: "))
i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1
print(fact)


