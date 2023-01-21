class EqualSignContext:
    def __init__(self):
        self.sign = "="

    def __enter__(self):
        print(self.sign*10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print(f"Error occured: {exc_val}")
            print(self.sign * 10)
        return True

with EqualSignContext():
    print("This code will be executed")
    x = 1 / 0
    print("This code will not be executed")

