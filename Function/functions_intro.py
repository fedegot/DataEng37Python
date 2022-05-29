######### DEFINE AND CALL A FUNCITON #############
# def greeting(name): #def = define a function
# print(f"Hello!, {name}!")
# return "Hello " + name + "!"

# WE NEED TO CALL THE FUNCTION
# greeting("Federico")
###################################################
# result = greeting("pippo") # assign a function to a variable
# print(result)

###################################################
# def greeting2(name="...you!"): #it will print ...you! if there is not parameter
#     return "Hello " + name
#
# print(greeting2())
###################################################
# print("one", "two", 6345, {})
#
# def multiargs(*args):
#     print(args, type(args))
#     for arg in args:
#         print(arg)
#
# multiargs(1, 2, 3)

# Define the function "product"
# It should accept any number of arguments
# and return the result from multiplying them all together

# def product(*pro):  # with the * you can insert as many parameter you want
#     if len(pro) == 0:
#         return None
#     else:
#         l = 1
#         for n in pro:
#             l *= n
#         return l
#
#
# print(product(5, 9, 10))

# If product is called with no arguments, return None


# def kwargs_demo(**kwargs): #Return as a DICTIONARY
#     print(kwargs, type(kwargs))
#
# print(kwargs_demo(a="one", b="Two"))

###################################################

# def calulate_tip(list_of_meals, total_cost, tip_pc):
#     print("You had: ")
#     for meal in list_of_meals:
#         print(meal)
#     print(f"Your total is: £{total_cost}")
#     print(f"With a {tip_pc:.0%} tip, the total is £{total_cost * (1 + tip_pc):.2f}")
#
# #TWO WAY TO CALL THE FUNCTION
# calulate_tip(["Burger", "Pizza"], 18.50, 0.1)
# #OR
# calulate_tip(
#     list_of_meals=["Pizza", "Burger", "Hot Dog"],
#     tip_pc=0.15,
#     total_cost=24
# )
################### KWARGS ##############################

# def calculate_total_cost(**meal_prices):
#     print(meal_prices, type(meal_prices))
#     #return total cost
#     s = 0
#     for i in meal_prices.values(): # LOOP IN THE MEAL PRICES and GET THE VALUES OF THE KEY
#         s += i
#     print(F"The total cost of the meal is {s}")
#
# calculate_total_cost(
#     Pizza=8.50,
#     Burger=9.00,
#     HotDog=9.20
# )

##################################################
def greeting(name: str):
    print("Hello " + name)

greeting("Fred")
##################################################
def division(denom: int, num: int) -> float:
    return denom / num

a = division(12, 3)
##################################################

#Good Functions
#1- Name them clearly, lowercase_with_underscores
#2- Clear argument name
#3- Functions that don't return somenthing return None
#4- Keep them small
#5- Use comments """ comments """
#6- Consider type hints

####### CALCULATE A FUNCTION INSIDE A FUNCTION #######
def fizzbuzz_line(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)

def fizzbuzz_game():
    for i in range(1, 101):
        print(fizzbuzz_line(i))

####### ####### ####### ####### ####### ####### #######