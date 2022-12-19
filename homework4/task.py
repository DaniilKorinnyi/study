text=input("Write your text: ")
if text.isdigit():
    if int(text) % 2 == 0:
        print("This is a number and it's even.")
    else:
        print("This is a number and it's odd.")
else:
    print("This is a word with a length of", len(text), "characters.")