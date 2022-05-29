# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("File has not been found")
#     print(errmsg)
#     raise # report all the errors
#
#
# # print(file, type(file))
# orders = file.readlines()
# print(orders)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# what if we want orders with the newline character
# app = []
# for x in orders:
#     app.append(x[:-1])
#
# print(app)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# data_job = map(lambda x : x[:-1], orders)
#
# print(list(data_job))
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ANOTHER WAY TO CLOSE A FILE
# with open("order.txt") as file:
#     raw_orders = file.readlines()
#     orders = list(map(lambda x: x.strip('\n'), raw_orders))
#
# print(file.closed)
#
# file.close()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# OPEN FILE E PRINT THE FIRST LINE
# with open("order.txt") as file:
#     orders = file.readline()
#
# print(orders)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# with open("order.txt") as file:
#     orders = file.read()
#
# print(orders, type(orders))
# order_list = orders.split('\n')
# print(order_list)
# print(file)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# with open("order.txt", "a") as file: # W stand to write A stand for append mode
#     file.write("This is the string to write\n")
#
# colours = ["Red\n", "Blue\n"]
#
# with open("order.txt", "a") as file: # W stand to write A stand for append mode
#     file.writelines(colours)

# Create a drinks menu text file
# Create a drinks orders text file
# Write a function that will take in a drink order
# If that order exists in the menu, write it to the order
# otherwise, raise an error
# add prices on the order if you have time

input = input("► Enter your order :\n► Or type menu for read the menù :\n")
found = False


def take_order(n):
    try:
        menu = open("drinks_menu.txt").readlines()
    except FileNotFoundError as errmsg:
        print("files not found")
        print(errmsg)
    menu2 = list(map(lambda x: x[:-1], menu))
    # search = list(map(lambda y : y == input, menu))
    if n == "menu":
        print(menu2)
    for x in menu2:
        if x == n:
            file = open("drinks_orders.txt", "a")
            file.write(f"{x}\n")
            print("Order added on the list!")
            file.close()
        if found:
            break

take_order(input)
