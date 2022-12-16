text = input("Enter some text: ")
char = text.split()

for char in text:
    if char.isdigit():
      if int(char) % 2 == 0:
        print(f"{char} is a number and it is even.")
      else:
        print(f"{char} is a number and it is odd.")
    elif char.isalpha():
      if char.isupper():
        print(f"{char} is a letter and it is uppercase.")
      else:
        print(f"{char} is a letter and it is lowercase.")
    else:
      print(f"{char} is a symbol.")