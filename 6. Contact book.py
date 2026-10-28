contacts_dict = {}

while True:
    temp = input("1 add, 2 search, 0 quit: ")

    if temp == "1":
        name = input("name: ")
        phone = input("phone: ")
        if name not in contacts_dict:
            contacts_dict[name] = phone

    elif temp == "2":
        name = input("name: ")
        if name in contacts_dict:
            print(contacts_dict[name])
        else:
            print("not found")

# implement choice 3 later
  
    elif temp == "0":
        break
