"""check whether the given number is prime or not using function"""

def prime(Number):
    count = 0
    i = 2
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and Number != 1):
        print(" %d is a Prime number" %Number)
    else:
        print(" %d is not a prime number" %Number)

Number = int(input(" Please Enter any Num: "))
prime(Number)





# Number = int(input(" Please Enter any Num: "))
# count = 0
# i = 2
# while(i <= Number//2):
#     if(Number % i == 0):
#         count = count + 1
#         break
#     i = i + 1
# if (count == 0 and Number != 1):
#     print(" %d is a Prime number" %Number)
# else:
#     print(" %d is not a prime number" %Number)