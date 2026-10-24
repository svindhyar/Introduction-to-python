a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if b == 0:
        print("division by zero error")
    else:
        print(a/b)
else:
    print("unknown operator", op)