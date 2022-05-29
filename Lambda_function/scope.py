# LEGB

# LOCAL - ( Local scope refers to the name(variable, function and so on) that is defined inside the function.
#           It means it is accessible within the point at it is defined until the end of the function.
#           That particular scope can’t be modified or even accessed outside the function. As an example,
#
#           def example():
#           x="LEGB rule"
#           print(x)
#
#           example()
#
#           print(x)
#           x variable can be accessible only inside the example() function so, when we attempt to use it as print(x)
#           it gives no error. However when we try to reach it from outside of the function(below we call example function),
#           there an error arises:
#
#           NameError: name 'x' is not defined LEGB rule
#
#           It is because, local scope isn’t visible outside the function where it is created. )

# ENCLOSED - (Enclosing scope is kind of scope that exists only in nested functions
#            (A function defined inside another function is called a nested function).
#            The enclosing scope is visible only for inner and enclosing functions. )

# GLOBAL  - (Global scope contains all the names(variables, functions, objects and so on) that you define at the highest
#           level in your program. It means that we can use that names from anywhere we wish.)


# str = "global function"
#
#
# def example():
#     def example_inner():
#         print(str)
#
#     print(str)
#
#     example_inner()
#
#
# example()
# Output
# will
# be as,
#
# global function
# global function


# BUILT-IN - ( ########################################################################## )
