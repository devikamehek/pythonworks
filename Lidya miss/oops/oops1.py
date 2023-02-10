class Emp:
    def display(self):
        print("OOPS : with self parameter self")
    x=100
    def sum(self,a,b):
        print("The sum is: ",a+b)
    def product(self,a,b):
        print("The product is: ",a*b)
    def disp():
        print("Without self parameter")



obj=Emp()
obj.display()
print("The value of the variable X is: ",obj.x)
obj.sum(20,40)
obj.product(2,4)
ob=Emp
ob.disp()

