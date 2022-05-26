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
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)


squ = Square(10)
print(squ.get_area())
print(squ.get_perimeter())

# print(str(squ.get_area()) + " This is your area of your square")
# print(str(squ.get_perimeter()) + " This is your perimeter of your square")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Create a Budget class that can keep track of different budget categories like food,
# clothing, and entertainment.
# These should allow for depositing and withdrawing funds from each category,
# as well computing category balances and transferring balance amounts between categories

# class Budget:
#     def __init__(self, food, clothing, entertaiment):
#         self.food = food
#         self.clothing = clothing
#         self.entertaiment = entertaiment
#         self._deposit = 0
#         self._withdrwaing = 0
#
#     def withdrwaing(self):
#         self._deposit -= self._withdrwaing
#         if self._deposit == 0:
#             return "You are bankrupt!"
#
#
#     def deposit(self, dep):
#         self._deposit += dep
#         return self._deposit
#
#     def __str__(self):
#         return f"Your budget on food is {self.food} /n Your budget on cloth is {self.clothing} /n Your budget on entertaiment is {self.entertaiment} /n Total Deposit {self._deposit} /n Total withdrwaing {self._withdrwaing}"
#
# pr = Budget(1000, 1001, 1002)
# pr.deposit(1000)
# print(pr._deposit)
# #pr.withdrwaing(50)
# print(pr)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# PILLARS OF OOP
#
# 1 - ABSTRACTION
# 2 - ENCAPSULATION
# 3 - INHERITANCE
# 4 - POLYMORPHISM



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# SOLUTION RECTANGLE
# class Rectange:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#
#     class Square(Rectange):
#         def __init__(self, length):
#             self.length = length
#             super().__init__(length, length)
#
#     s = Square(s)
#     print(s.get_area())
#     print(s.get_perimeter())



