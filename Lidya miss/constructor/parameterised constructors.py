class A:
    def __init__(self,name):
        print("Parameterised Constructor")
        self.na=name
    def display(self):
        print("Name is: ",self.na)

obj=A("mrunal")
obj.display()