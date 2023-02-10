class Emp:
    def read(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print("The sum is: ",self.x+self.y)
    def product(c):
        print("The product is: ",c.x*c.y)


obj=Emp()
obj.read(2,3)
obj.sum()
obj.product()




class Fruits:
    def read(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print("Sum: ",self.a+self.b)

obj1=Fruits()
obj1.read(5,3)
obj1.sum()
