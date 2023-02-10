n=int(input("Enter the num: "))
n1=0
n2=1
sum=0
while(n1<n2):
    sum=n1+n2
    n1=n2
    n2=sum
    print(n1)