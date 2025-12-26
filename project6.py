from abc import ABC, abstractmethod
class Shapes (ABC):
    def init(self):
        pass
    def calculate_area():
        pass
    def calculate_perimeter():
        pass
    @abstractmethod
    def getTheSizeOfTheSides(self):
        pass


class Rectangle(Shapes):
    def init(self,height,width):
        self.height=height
        self.width=width

    def calculate_area(self):
        return(self.height*self.width)

    def calculate_perimeter(self):
        return(2*self.height)+(2*self.width)
    
    def getTheSizeOfTheSides(self):
        return 3




class Circle(Shapes):
    def init(self,radius):
        self.radius=radius

    def calculate_area(self):
        return(self.radius*self.radius*3.14159)
        
    def calculate_perimeter(self):
        return(self.radius+self.radius)*3.14159

    def getTheSizeOfTheSides(self):
        return 0
    


shapes=[]
    
r1=Rectangle(20,10)
c1=Circle(3)


shapes.append(r1)
shapes.append(c1)


print(" ")


for shape in shapes:
    print(" ")
    print(f"the area for shapes : {shape.calculate_area()}")
    print(" ")
    print(f"the perimeter for shapes : {shape.calculate_perimeter()}")
    print(" ")
    print(f"the Sides for shapes : {shape.getTheSizeOfTheSides()}")
    print(30 * "-")