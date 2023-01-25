import json

def load_phonebook(file_name):
    try:
        with open(file_name, 'r') as f:
            phone_book = json.load(f)
            return phone_book
    except FileNotFoundError:
        return {}

def save_phonebook(file_name, phone_book):
    with open(file_name, 'w') as f:
        json.dump(phone_book, f)

file_name = 'phone_book.json'
phone_book = load_phonebook(file_name)

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
            save_phonebook(file_name, phone_book)
            print(phone_book)
    def delete():
        print("Write name: ")
        name = input()
        if name in phone_book:
            del phone_book[name]
            save_phonebook(file_name, phone_book)
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
        if name in phone_book:
            print(phone_book.get(name))
        else:
            print("There isn't such name in your phone book.")
    else:
        print("Command not found")