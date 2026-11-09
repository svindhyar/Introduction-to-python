N = int(input("N: "))
for i in range(1, N + 1):
    if i % 15 == 0:
        print("fizzbuzz", end=" ")
    elif i % 3 == 0:
        print("fizz", end=" ")
    elif i % 5 == 0:
        print("buzz", end=" ")
    else:
        print(i, end=" ")