# alphabet = ["A", "B", "C", "D", "E"]
#
# for letter in alphabet:
#     print("The next letter is:")
#     print(letter.lower())
#     if letter == "D":
#         print("Oh no!")
#     else:
#         print("Horray!")


# nest = [[1,2,3],[4,5],[6,5,8,9]]
#
# for sublist in nest:
#     print(sublist)
#     for number in sublist:
#         print(number)

##################################
# hi = "hello world"
#
# for x in i:
#     print(x)


########################

#
#
# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
#
# for key in a_dict:
#     print(key)
#
# for key in a_dict.values():
#     print(key)

data_eng_37 = {
        "course_name": "Data Engineering 37",
        "client": "Home office",
        "trainer": {
            "name": "David",
            "energy_level": "low"
        }
    }

# for x in data_eng_37:
#     print(x)
#
# for x in data_eng_37:
#     print(x)
#     print(data_eng_37[x])


for key, value in data_eng_37.items():
    print(f"The {key} is {value}")


########################


for x in range(5):
    print(x+1)

for x, key in enumerate(data_eng_37):
    print(x, key)


