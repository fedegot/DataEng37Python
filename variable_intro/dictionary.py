data_eng_37 = {
    "course_name": "Data Engineering 37",
    "client": "Home office",
    "trainer": {
        "name": "David",
        "energy_level": "low"
    }
}

# print(data_eng_37, type(data_eng_37))
#
 # print(data_eng_37["client"]) # dictionary name [key]
 # data_eng_37["trainer"] = "David Harvey"
 # data_eng_37["trainees"] = ["Munir", "Darnell", "Pippo"]

print(data_eng_37["trainer"]["energy_level"])


data_eng_37.update({"course_length": "8 Weeks"})
print(data_eng_37)


DieHard= {
    "Movie Name": "Die hard",
    "Gendre": "Action",
    "Time": "210",
    "Located": "Miami USA",
    "BoxOffice": "12bln",
    "MainCharacter": {
        "Real Name": "Bruce Willis",
        "OtherMovies": {
            "NameMovie": "Armageddon",
        },
        "Character Name": "John McClane",

    },
    "SecondCharacter": {
        "Real Name": "Alan Rickman",
        "OtherMovies": {
            "NameMovie": "Harry Potter and the Philosopher's Stone",
        },
         "Character Name": "Hans Gruber",
    },
}




