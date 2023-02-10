def fact(n):
    if n==1:
        return n
    else:
        x= n*fact(n-1)
        return x

n=int(input("enter the number: "))
print(fact(n))