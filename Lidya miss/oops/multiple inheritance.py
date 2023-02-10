# A-base class
# B-base class
# C-parent class

class A:
    def person(self):
        self.name=input("Enter the Name: ")
        self.age=int(input("Enter Age: "))
class B:
    def job(self):
        self.area=input("Enter the course: ")
class C(A,B):
    def details(self):
        print("The Details: ",self.name,self.age,self.area)

obj=C()
obj.person()
obj.job()
obj.details()