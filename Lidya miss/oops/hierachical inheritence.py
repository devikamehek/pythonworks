# a-read
# b-sum
# c-average
# d-product

class A:
    def read(self):
        self.x=int(input("enter x: "))
        self.y=int(input("enter y: "))
class B(A):
    def sum(self):
        self.s=self.x+self.y
        print("Sum is: ",self.s)
class C(A):
    def average(self):
        self.a=self.x+self.y
        print("Average is: ",(self.a)/2)
class D(A):
    def product(self):
        self.p = self.x + self.y
        print("Product is: ",self.p)

obj1=B()
obj1.read()
obj1.sum()

obj2=C()
obj2.read()
obj2.average()

obj3=D()
obj3.read()
obj3.product()
