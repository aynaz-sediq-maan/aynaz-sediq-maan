from abc import ABC, abstractmethod


class Shape (ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area():
        pass
    
    @abstractmethod
    def calculate_perimeter():
        pass


class Rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return (2 * self.height) + (2 * self.width)




class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2) 
        
    def calculate_perimeter(self):
        return 3.14159 * (2 * self.radius)
    





height_Rectangle1=int(input("please input height: "))
width_Rectangle1=int(input("please input width: "))

Rectangle1=Rectangle(height_Rectangle1,width_Rectangle1)




radius1=int(input("please input radius: "))

Circle1=Circle(radius1)


ListsShape=[Rectangle1,Circle1]


i=0
print("\n")
for Shapes in ListsShape:
    Area=Shapes.calculate_area()
    Perimeter=Shapes.calculate_perimeter()
    i=i+1
    print(f"the Area for shape {i} : {Area}\nthe Perimeter for shape {i} : {Perimeter}\n")