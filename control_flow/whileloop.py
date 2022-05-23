# x = 0
#
# while x < 10:
#     print(f"While loop running: {x}")
#     if x == 5:
#         break #loop stop
#     x += 1

#### lets do some fizz and buzz


# count = 0
#
# while count < 101:
#     if (count % 5) == 0 and (count % 3) == 0:
#         print("FizzBuzz")
#         count = count +1
#     elif(count % 3) == 0:
#         print("Fizz")
#         count = count + 1
#     elif (count % 5) == 0:
#         print("Buzz")
#         count = count +1
#     else:
#         print(count)
#         count = count + 1

#@@@@@@@@@@@@@@@ AGE CONFIRMATION WITH WHILE LOOP @@@@@@@@@@@@@@@
keep_asking = True

while keep_asking:
    age = input("What is your age?\n")
    if age.isdigit():
        age_int = int(age)
        keep_asking = False
    else:
        print("Please enter a valid number in digits.")

print(f"Your Age is {age_int}")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@