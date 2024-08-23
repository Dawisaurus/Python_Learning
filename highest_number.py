import random

random_number_to_guess = random.randint(1, 100)
player_guess = 0
print("Enter a number between 1 and 100")

while player_guess != random_number_to_guess:
    player_guess = int(input("Enter your guess: "))
    if player_guess < random_number_to_guess:
        print("Number is higher!")
    elif player_guess > random_number_to_guess:
        print("Number is lower!")
    else:
        print("Correct answer!")
