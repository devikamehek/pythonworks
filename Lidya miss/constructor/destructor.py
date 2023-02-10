class A:
    def __init__(self,name):
        print("Parameterised Constructor")
        self.na=name
    def __del__(self):
        print("destructor")


obj=A("mrunal")
del obj
