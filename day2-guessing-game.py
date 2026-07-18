import random

# Load high score from file
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = float('inf')

secret = random.randint(1, 10)
guesses = 0

while True:
    guess = int(input("Guess a number between 1-10: "))
    guesses += 1
    
    if guess == secret:
        print(f"You got it in {guesses} tries!")
        if guesses < high_score:
            print(f"New high score! Previous was {high_score}")
            with open("highscore.txt", "w") as f:
                f.write(str(guesses))
        else:
            print(f"High score is still {high_score}")
        break
    elif guess < secret:
        print("Too low, try again")
    else:
        print("Too high, try again")
