import json

phone_book_dict = {}
try:
    with open('telephonebook', 'r') as file:
        phone_book_dict = json.load(file)
except:
    pass

def add(name, number):
    phone_book_dict[name] = number
    with open('telephonebook', 'w') as file:
        json.dump(phone_book_dict, file)

def delete(name):
    del phone_book_dict[name]
    with open('telephonebook', 'w') as file:
        json.dump(phone_book_dict, file)

def update(name, number):
    phone_book_dict[name] = number
    with open('telephonebook', 'w') as file:
        json.dump(phone_book_dict, file)
while True:
    a = input("What do you want to do (add/delete): ")
    if a == "add":
        name = input("Write name: ")
        number = input("Write number: ")
        add(name, number)
        print(phone_book_dict)
    elif a == "delete":
        name = input("Write name: ")
        delete(name)
        print(phone_book_dict)