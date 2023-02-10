"""reverse of a number using while loop"""

# a=int(input("enter the number: "))
# rev=0
# while(a>0):
#     r= a % 10
#     rev= (rev*10)+r
#     a=a//10
# print("Reverse number is: ",rev)

n=12345
rev=0
p=1
sum=0
while(n>0):
    r=n%10
    rev=(rev*10)+r
    p = p * r
    sum = sum + r
    n=n//10 #reverse

print("reverse is: ",rev)
print("product is: ",p)
print("sum is: ",sum)

#sum
# a=12
# rev=0
# sum=0
# while(a>0):
#     r=a%10
#     rev=(rev*10)+r
#     sum=sum+r
#     a=a//10
# print(sum)







