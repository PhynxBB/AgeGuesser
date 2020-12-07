year = input("Current Year: ")
# declaring a string variable based on user input
birth_year = input("Birth Year: ")
# declaring a string variable based on user input
has_passed = input("Have you had your birthday this year?: ")
# declaring a string variable based on user input
if str.lower(has_passed) == "yes":
    age = int(year) - int(birth_year)
    print(age)
    # making user input case insensitive, parsing strings into integers for calculation
elif str.lower(has_passed) == "no":
    age = int(year) - 1 - int(birth_year)
    print(age)
    # making user input case insensitive, parsing strings into integers for calculation
else:
    print("Please answer with either yes or no")
    # an option for typos / incorrect answer formatting




