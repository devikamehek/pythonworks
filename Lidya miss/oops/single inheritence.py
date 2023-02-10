class A:
    def displayA(self):
        print("Base class method")
class B(A): # A is derived to B
    def displayB(self):
        print("Derive Class method")

obj=B()
obj.displayA()
obj.displayB()

#here object is created for class B. thus A is derived to B thus calling B also calls A



class A:
    def read(self):
        print("Sum of 2 Numbers")
        self.x=int(input("enter x: "))
        self.y=int(input("enter y: "))
class B(A):
    def sum(self):
        print("sum is: ",self.x+self.y)

ob=B()
ob.read()
ob.sum()


