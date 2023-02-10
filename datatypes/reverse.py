"""reversing a number using while loop"""
n=int(input("enter the number: "))
reverse_number=0
while(n>0):
    remainder=n % 10
    reverse_number=(reverse_number*10)+remainder
    n=n//10
print(f'reverse of the number  is ',reverse_number)

"""method 2
string conversing
"""
