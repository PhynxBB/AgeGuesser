from random import randint
low_number = int(input("Please input the lowest number: "))
high_number = int(input('Please input the highest number: '))
random_int = randint(low_number, high_number)
max_guesses = int(input("How many guesses would you like: "))
guesses = 0
while guesses < max_guesses:
    user_guess = int(input("Guess a number " + str(low_number) + " - " + str(high_number) + ": "))
    if user_guess == random_int:
        print("Correct!")
        break
    elif user_guess < random_int:
        print("Higher!")
    elif user_guess > random_int:
        print("Lower!")
    guesses += 1
if guesses == max_guesses and user_guess != random_int:
    print("Maybe next time!")






