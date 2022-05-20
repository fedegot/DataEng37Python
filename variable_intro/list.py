shopping_list = ["bread", "bananas", "biscuits"]
#
# print(shopping_list, type(shopping_list))
#
# # indexing and slicing
# print(shopping_list[0])
# print(shopping_list[-1])
# print(shopping_list[::1])
#
# # list and Mutable
# shopping_list[0] = "sugar"
# print(shopping_list)
#
# # append ad an item at the end of the list
shopping_list.append("cereal")
print(shopping_list)
shopping_list.append("chocolate")

print(len(shopping_list))
# remove a item from the list, the first one
shopping_list.remove("biscuits")
print(shopping_list)


hi = "hello"
print(hi.upper())
print(hi)
print(shopping_list)
print(shopping_list.pop())
print(shopping_list)

mixed_list = [1,2,3,4,44, "ciao"]
print(mixed_list)


nested_list = [[1123,123,321], [123,33,22,11],[139,22,33]]
print(nested_list[1][1])

print(shopping_list.count("bananas"))
print(shopping_list.index("bread"))
