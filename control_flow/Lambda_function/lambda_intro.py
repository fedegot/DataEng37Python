# LAMBDA OR ANONYMOUS FUNCTION

# addition = lambda num1, num2: num1 + num2 + 1
# print(addition(5, 7))

# @#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#

# map
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
# saving = [242.00, 22.00, 50.00, 31.32]
# bonus_lambda = list(map(lambda x: x * 1.1, saving))
# print(bonus_lambda)
# print(list(f"{sb:.2f}" for sb in saving))

# @#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#

# Use map and lambda to create a list of each number squared plus 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = map(lambda x: (x ** 2) + 3, numbers)
print(list(ans))

evens = filter(lambda x: x % 2 == 0, ans)
print(list(evens)) # FILTER( wants to return a function which return a boolean

# @#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#

jobs = ["Data Analyst", "C#  Developer", "Data Engineer", "DevOps Engineer", "Data Architect"]
# using map and filter with lambdas
# product a list of the database roles without the word data in there
# i.e. ["Analyst", "Engineer", "Architect"]

eng = filter(lambda x: "Engineer" in x, jobs)
analyst = filter(lambda x: "Analyst" in x, jobs)
dev = filter(lambda x: "Developer" in x, jobs)

data_job = map(lambda x: x[4:], jobs)

#eng = filter(lambda y: y == True, ans2)
print(list(data_job))
print(list(eng))
print(list(analyst))
print(list(dev))










