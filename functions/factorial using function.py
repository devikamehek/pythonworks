"""write a program to find the factorial of a number using function"""



def factorial(n):
    i = 1
    fact = 1
    while (i <= n):
        fact = fact * i
        i = i + 1
    print(fact)

n=int(input("Enter the number: "))
factorial(n)







# a=int(input("Enter the number: "))
# fact=1
# i=1
# while(i<a):
#     fact=fact*i
#     i=i+1
# print(fact)
