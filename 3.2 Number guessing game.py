import random

secret = random.randint(1,10)
guess = int(input("Your guess: "))
while guess != secret:
    if guess < secret:
        print("too low")
    else:
        print("too high")
    guess = int(input("Your guess: "))
print("Success: ")