import random

def hello():
    print("Hello! What is your name?")
    name = input()

    print(f" Well, {name}, I am thinking of a number between 1 and 20.")
    while True:   
        print("Take a guess.")

        x = int(input())
        x1 = random.randint(1, 20)
        if x == x1:
            print(f"Good job, {name}! You guessed my number in {x} guesses!")
            break
        print("Your guess is too low.")
