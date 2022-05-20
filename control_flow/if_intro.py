# age = 14
# has_ticket = True
#
# if age >= 15 and has_ticket:
#     print("You can watch this film")
# elif age == 14 and has_ticket:
#     print("Come back next year")
# else:
#     print("You need to be at least 15 and have a ticket")

#
# # U, PG, 12 / 12A, 15, 18
# age = 14
# film_rating = "12A"
#
# if film_rating == "U" and age >= 4:
#     print(f"You can watch this film you are only {age} for movie {film_rating}")
# elif film_rating == "PG" and age >= 8:
#     print(f"You can watch this film you are {age} for movie {film_rating}")
# elif film_rating == "12A" and age >= 13:
#     print(f"You can watch this film you are {age} for movie {film_rating}")
# elif film_rating == "15" and age >= 15:
#     print(f"You can watch this film you are {age} for movie {film_rating}")
# elif film_rating == "18" and age >= 18:
#     print(f"You can watch this film you are {age} for movie {film_rating}")


#    NESTED IF STATEMENT
age = 13
has_ticket = True

if has_ticket:
    if age>= 15:
        print("You can see this film.")
    else:
        print("Come back when you're older.")
else:
    print("You need a ticket - go buy one!")