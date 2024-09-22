 guessing game 
 command = ""
 while command.lower() != "quit":
     command = input("> ").lower()
     if command == "start":
        print("you are ready to go!")
     elif command == "stop":
         print("car is going to stop!")
     elif command == "help":
         print("start :- you are ready to go" "stop :- car is going yo stop")
     else:
        print("sorry! I don't understand.")

#This is a another method
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter Numbers Between 1 to {x} :'))
        if guess < random_number:
            print("Sorry! try once. too low")
        elif guess > random_number:
            print("Sorry! try once. too high")

    print(f'congratulation! you have guessed it {random_number} correctly.')

guess(10)

# another method

import random

def computer_guess (x):
    low = 1
    high = x
    feedback= ""
    while feedback != 'c':
        if low!=high:
         guess = random.randint(low,high)
        else:
            low=high
        feedback = input(f'is {guess} is too high (H), is too low (L) or Correctly: ').lower()
        if feedback=='h':
            guess -= 1
        if feedback=='l':
            guess += 1
            print(f'yah! your computer guessed it {guess} correctly!')

computer_guess(10)
