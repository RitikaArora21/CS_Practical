'''18. Write a program to implement a class for finding area and perimeter of a 
rectangle. Write constructor, destructor, and functions for calculating area and 
perimeter.'''
class rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2*(self.l + self.b)

l = int(input("Enter length (in m):"))
b = int(input("Enter breadth (in m):"))
obj = rectangle(l,b)
print("Area of rectangle is:", obj.area())
print("Perimeter of rectangle is:",obj.perimeter())
