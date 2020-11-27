import random

secret = random.randrange(1,101)
print(secret)

guess = 0
while guess != secret:
    guess = int(input("Make a guess: "))

    if guess > secret:
        print("Too High!")
    elif guess < secret:
        print("Too Low!")
    else:
        print("You got it!")
