items = ["milk", "eggs", "bread"]

with open("shopping_list.txt", "w", encoding="utf-8") as f:
    for item in items:
        f.write(f"{item}\n")
with open("shopping_list.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")

    
    