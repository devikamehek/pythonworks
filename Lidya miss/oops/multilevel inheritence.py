class A:
    def read(self):
        self.x=int(input("enter x: "))
        self.y=int(input("enter y: "))
class B(A):
    def sum(self):
        print("Sum is: ",self.x+self.y)
class C(B):
    def average(self):
        print("Average is: ",(self.x+self.y)/2)

ob=C()
ob.read()
ob.sum()
ob.average()

#here object created  for C