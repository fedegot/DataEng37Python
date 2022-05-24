# class Dog:  # Capital letter for the Class
#     animal_type = "Canine"  # CLASS VARIABLE
#
#     def bark(self):  # SELF mean current class, THIS IS A METHOD
#         return f"Woof! I am a {self.animal_type}"
#
#
# fido = Dog()  # Calling the class, INSTANTIATION = CREATING AN INSTANCE OF THE CLASS
# print(fido.animal_type)
# print(fido.bark())
#
# lassie = Dog()
# print(lassie.animal_type)
# print(lassie.bark())
#
# Dog.animal_type = "arachnid"  # Update class variable
# Dog.legs = 8
#
# print(lassie.legs)
# print(lassie.animal_type)
#
# print(fido)
# print(type(fido))


######################################################
# class Dog:
#     def __init__(self):  # initialise, with this the characteristic they are not affected after declare the CLASS
#         self.animal_type = "canine"
#         self.legs = 4
#
#     def bark(self):
#         return f"Woof! I am a {self.animal_type}"


######################################################
# class Dog:
#     def __init__(self, name,
#                  colour):  # initialise, with this the characteristic they are not affected after declare the CLASS
#         self.animal_type = "Canine"
#         self.legs = 4
#         self.name = name
#         self.colour = colour
#
#     def bark(self):
#         return f"Woof! I am a {self.animal_type}"
#
#
# fido = Dog("Fido", "Black")
# print(fido.animal_type)
# print(fido.name)
# print(fido.colour)
######################################################

# class Spartan:
#     def __init__(self, name, course_name, course_number, course_length):
#         self.name = name
#         self.course_name = course_name
#         self.course_number = course_number
#         self.course_length = course_length
#
#     def motivation(self):
#         return f"Hello I am Federico and I am studying in the {self.course_name} n. {self.course_number}  for the next {self.course_length} weeks"
#
#
# Federico = Spartan("Federico", "Data Eng", "37", "8")
#
# Mark = Spartan(  # won't work this one because the class is def __init__
#     name="Mark",
#     course_name="Data Eng",
#     course_number="37",
#     course_length="8"
# )
#
# print(Federico.motivation())
# print(Mark.motivation())  # won't work this one because the class is def __init__


############################################################################################################

# CLASS A CLASS TO REPRESENT A CAR
# MAKE, MODEL, TOP_SPEED
# speed should start at 0

# accelerate method - takes a speed in mph and adds it to the current speed
# break method - takes a speed and subtracts it from current speed


class Car:
    def __init__(self, make, model, top_speed):
        self.speed_add = None
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.speed = 0

    def accelerate(self, speed):
        self.speed += speed

    def brake(self, brake):
        self.speed -= brake


MyCar = Car("BMW", "118d", 170)
MyCar.accelerate(40)
MyCar.brake(20)

print(MyCar.speed)
