# #n=int(input("enter the year: "))
# if(n%4==0) and (n%1==0):
#     print(f'{n} is a leap year')
# else:
#     print(f'{n} is not a leap year')

year=int(input("enter the year: "))
#divided by 100 is a century year
#century year divided by 400 is a leap year
if(year%400==0) and (year%100==0):
    print(f'{year} is a Leap year')
#year not divided by 100 is not a century year
#year divided by 4 is a leap year
elif(year%4==0) and (year%100!=0):
    print(f'{year} is a Leap year')

else:
    print(f'{year} is not a Leap year')