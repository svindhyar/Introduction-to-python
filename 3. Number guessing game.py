import random

secret = random.randint(1, 100)

attempts = 0
while attempts < 7:
    guess = int(input("guess your number: "))
    attempts = attempts + 1

    if guess == secret:
        print("success")
    elif guess < secret:
        print("too low")
    elif guess > secret:
        print("too high")

if guess != secret:
    print("lost the game", secret)

