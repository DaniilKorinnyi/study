# ======== additional tasks=======

# ==== task 3 ====
class MyStr:
    def __init__(self, str):
        self.str = str
    def __str__(self):
        return self.str.upper()
my_str = MyStr("hello")
print(my_str)