shopping_list = ["bread", "bananas", "biscuits"]

print(shopping_list, type(shopping_list))

# indexing and slicing
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[::1])

# list and Mutable
shopping_list[0] = "sugar"
print(shopping_list)

# append ad an item at the end of the list
shopping_list.append("cereal")
print(shopping_list)
shopping_list.append("chocolate")

print(len(shopping_list))
# remove a item from the list, the first one
shopping_list.remove("biscuits")
print(shopping_list)
