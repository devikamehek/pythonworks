class A:
    def sum(self,a):
        print("Sum is: ",a+a)
    def sum(self,a,b):
        print("Sum is: ",a+b)

ob=A()
# ob.sum(10) it will not work
ob.sum(10,20)

"""python does not support function overloading. here the second function works."""

class A:
    def display(self,name=None):
        if name is None:
            print("hello")
        else:
            print("hello",name)


obj=A()
obj.display()
obj.display("mrunal")

"""here the last function only works. if we give three function with same name and arguments only the last 
function will work."""