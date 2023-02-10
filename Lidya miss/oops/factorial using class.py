"""factorial using class with function"""

class Factorial:
    def fact(self):
        f=1
        n=int(input("Enter num: "))
        for i in range(1,n+1):
            f=f*i
            i=i+1
        print("Factorial is: ",f)

obj=Factorial()
obj.fact()

#using return value

class Emp:
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f

obj=Emp()
n=int(input("Enter the number: "))
f=obj.fact(n)
print("Factorial is: ",f)