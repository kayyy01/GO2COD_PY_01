import random
Print("Welcome to The Number Guessing Game")

number = random.randint(1, 100)
guess = 0
attempts = 0 #initialize attempts


while guess != number:
    guess = int(input("Guess a number between 1 and 100:"))
    attempts += 1  #increments attempts with each guess

    if guess < number:
        print("Guess higher!")
    elif guess > number:
        print("Guess lower!")
    else: 
        print("You got it! The number was",number)
        print(f"It took you {attempts} attempts to guess the number")    



