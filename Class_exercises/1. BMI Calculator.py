weight = float(input("weight (kg): "))
height = float(input("height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"
print(f"bmi: {bmi:.1f} ({category})")