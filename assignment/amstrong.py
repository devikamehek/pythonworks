n=int(input("enter the number: "))
sum=0
temp=n #initialize n to temp
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if(n==sum):
    print(f'{n} is an Amstrong Number')
else:
    print(f'{n} is not an Amstrong Number')
