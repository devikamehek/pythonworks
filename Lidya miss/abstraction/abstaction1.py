from abc import ABC ,abstractmethod
#abstract class
class polygon(ABC):

    #abstract method
    @abstractmethod
    def sides(self):
        pass #abstract method, which contain only declaration
    def display(self):
        print("non abstract method - that contain complete definition")

class triangle(polygon):
    def sides(self):
        print("Triangle has 3 sides")

obj=triangle()
obj.sides()
obj.display()