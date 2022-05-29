import json
#
# car_data = {
#     "make": "Tesla",
#     "type": "Electric",
#     "faults": 3896,
#     "death_trap": True,
#     "driver": None
# }
#
# #print(car_data["faults"], type(car_data))
#
# dumps = json.dumps(car_data)
# print(dumps, type(dumps))
# # WRITE A JSON FILE WITH THE DICTIONARY
# with open("tesla.json", "w") as jsonfile:
#     json.dump(car_data, jsonfile)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ REVERSE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

with open("sparta.json") as jsonfile:
    spartan = json.load(jsonfile)

print(spartan, type(spartan))
