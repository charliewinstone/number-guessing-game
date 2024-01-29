import random

#Establish general housekeeping variables
numbers = [i for i in range(1, 101)]
number = random.choice(numbers)
guesses = 0 #Set to 0 as placeholder int
guess = 0 #Set to 0 as placeholder int, specifically 0 as this is not in the range of numbers in the game and therefore allows the game to play without conflictions

#Introduce player to game, decide which mode to play
print("Welcome to number guesser! I'm thinking of a number between 1 and 100, you'll have a certain amount of guesses to see if you can get it right!")
answer = input("Would you like to play on easy or hard mode?\n")

#Set number of guesses to corresponding difficulty, inform player of how many guesses they now have
if answer == "easy":
    guesses = 10
    print(f"Okay, you'll have {guesses} guesses on easy mode!")
elif answer == "hard":
    guesses = 5
    print(f"Okay, you'll have {guesses} guesses on hard mode!")

#Check if guess matches number, react accordingly depending on whether it's too high, too low or correct
def number_check(guess, number, guesses):
    if guess < number:
        print(f"You were too low and now only have {guesses} guesses remaining!")
    elif guess > number:
        print(f"You were too high and now only have {guesses} guesses remaining!")
    elif guess == number:
        print("Congratulations! You guessed it!")

#Function to run the while loop/game - whilst player's guess is incorrect, it will keep running until guesses reaches 0
def play():
    global guess
    global guesses
    while guess != number:
        if guesses == 0:
            print(f"You have run out of guesses :( the number was {number}")
            break
        else:
            guess = int(input("What number would you like to guess?\n"))
            guesses -= 1
            number_check(guess, number, guesses)

#Function called to play the game
play()
