grade = float(input("grade/20: "))

if grade < 0 or grade > 20:
    print("Invalid grade")
elif grade >= 16:
    print("very good")
elif grade >=14:
    print("good")
elif grade >=12:
    print("fairly good")
elif grade >=10:
    print("Pass")
else:
    print("Fail")
    