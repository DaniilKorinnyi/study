
# ==== task 4 ====

class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()
name1 = User("dania")
name2 = User("DANIA")
name3 = User("Denis")
print(name1 == name2)