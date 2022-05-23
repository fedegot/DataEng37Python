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
# keep_asking = True
#
# while keep_asking:
#     age = input("What is your age?\n")
#     if age.isdigit():
#         age_int = int(age)
#         keep_asking = False
#     else:
#         print("Please enter a valid number in digits.")
#
# print(f"Your Age is {age_int}")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#FIZZBUZZ WITH INPUT NORMAL LOOP

count = input("Please enter the number to FizzBuzz up to: ")
count = int(count)

for i in range(1, count):
    if (i % 5) == 0 and (i % 3) == 0:
        print("FizzBuzz")
        i = i +1
    elif(i % 3) == 0:
        print("Fizz")
        i = i + 1
    elif (i % 5) == 0:
        print("Buzz")
        i = i +1
    else:
        print(i)
        i = i + 1

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#FIZZBUZZ WITH INPUT WITH WHILE LOOP


cou = input("please insert a number where to start to count from \n")
cou = int(cou)

while cou < 101:
    if (cou % 5) == 0 and (cou % 3) == 0:
        print("FizzBuzz" + " " + str(cou))
        cou = cou + 1
    elif(cou % 3) == 0:
        print("Fizz" + " " + str(cou))
        cou = cou + 1
    elif (cou % 5) == 0:
        print("Buzz" + " " + str(cou))
        cou = cou +1
    else:
        print(cou)
        cou = cou + 1

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
