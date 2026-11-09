direction = input("convert to C or F?")
temperature = float(input("Temperature:"))

if direction == "C":
    result = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", round(result, 2))

elif direction == "F":
    result = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(result, 2))

else:
    print("unknown direction")