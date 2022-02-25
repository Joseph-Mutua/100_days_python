programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "Piece of code that runs repeatedly"

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A roach that has invaded your laptop"

# print(programming_dictionary)


# Loop through a dictionary
for key in programming_dictionary:
    print(key)


# First Coding Project
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)


# Nesting Lists and Dictionaries
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": {"cities_visited": ["Hamburg", "Berlin", "Stuttgart"]},
}

# Nesting Dictionaries inside a list
travel_log = [
    {
        "country": "France",
        "cities_visited":  ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    }, {
        "country": "Germany",
        "cities_visited":  ["Hamburg", "Berlin", "Stuttgart"],
        "total_visits": 5
    }
]


# Dictionary in List
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
