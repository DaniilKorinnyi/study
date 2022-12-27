phone_book_list = [
    ["Kate", "+096231453"],
    ["Jack", "+097312414"],
    ["Alice", "+063672317"]
]
phone_book = dict(phone_book_list)

while True:
    print("What do you want to do: ")
    b = input()

    def add():
        print("Write name: ")
        name = input()

        if name in phone_book:
            print("Such name has already exist.")
        else:
            print("Write his/her number: ")
            c = input()
            phone_book[name] = c
            print(phone_book)
    def delete():
        print("Write name: ")
        name = input()
        if name in phone_book:
            del phone_book[name]
            print(phone_book)
        elif phone_book.get(name) is None :
            print(f"{name} doesn't exist.")

    if b == "add":
        add()
    elif b == "delete":
        delete()
    elif b == "stat":
        stats = len(phone_book)
        print(f"You have {stats} contacts in your phonebook")
    elif b == "list":
        print(phone_book)
    elif b == "show":
        print("Write name: ")
        name = input()
        print(phone_book.get(name))
    else:
        print("Command not found")