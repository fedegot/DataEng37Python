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

def product(*pro):  # with the * you can insert as many parameter you want
    if len(pro) == 0:
        return None
    else:
        l = 1
        for n in pro:
            l *= n
        return l


print(product(5, 9, 10))

# If product is called with no arguments, return None
