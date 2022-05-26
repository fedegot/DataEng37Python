# LAMBDA OR ANONYMOUS FUNCTION


# addition = lambda num1, num2: num1 + num2 + 1
# print(addition(5, 7))

# @#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
#map
# saving = [242.00, 22.00, 50.00, 31.32]
# # bonus = saving with 10% added on
#
# bonus = []
# for x in saving:
#     bonus.append(x+(x*0.1))
# print(bonus)
# @#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
# saving = [242.00, 22.00, 50.00, 31.32]
# def apply_bonus(saving):
#     return saving * 1.1
#
# bonus_map = list(map(apply_bonus, saving))
# print(bonus_map)

# @#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#

# MAP with LAMBDA
saving = [242.00, 22.00, 50.00, 31.32]
bonus_lambda = list(map(lambda x: x * 1.1, saving))
print(bonus_lambda)

# @#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
