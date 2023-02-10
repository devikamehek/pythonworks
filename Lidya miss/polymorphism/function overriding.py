class rectangle: #base class
    def area(self,l,b):
        print("Area of rectangle is: ",l*b)

class square(rectangle): #derived class
    def area(self,l,b):
        print("Area of square is: ",l+b)

obj=square()
obj.area(10,20)



