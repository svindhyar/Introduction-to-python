def ask_int(message):
    while True:
        text = input(message)
        try:
            return int(text)
        except ValueError:
            print("please type a number")

age = ask_int("Age:")
print("next year you will be", age + 1)