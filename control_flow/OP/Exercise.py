# Please create the following:
#
# - A rectangle class
# - It should have a width and a height
# - Give it the methods: get_area() and get_perimeter()
# - Give it appropriate str and repr representations
#
# - A square class
# - It should have a length
# - It needs get_area() and get_perimeter() and appropriate str and repr representations

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        self.height * self.width

    def get_perimeter(self):
        (self.height * 2) + (self.width * 2)

    def __repr__(self):
        return f"If your height is {self.height} and your width is {self.width} your area it will be {self.height * self.width}."

    def __str__(self):
        return f"If your height is {self.height} and your width is {self.width} your perimetr will be {(self.height * 2) + (self.width * 2)}."


sq1 = Rectangle(10, 5)
print(sq1)
print(repr(sq1))


class Square(Rectangle):
    def __init__(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.height

    def get_perimeter(self):
        return self.height * 4


squ = Square(10)
print(str(squ.get_area()) + " This is your area of your square")
print(str(squ.get_perimeter()) + " This is your perimeter of your square")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# PILLARS OF OOP
#
# 1 - ABSTRACTION
# 2 - ENCAPSULATION
# 3 - INHERITANCE
# 4 - POLYMORPHISM