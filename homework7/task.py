def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

def get_fibonacci_number(n):
    for i, f in enumerate(fibonacci()):
        if i == n:
            return f

n = int(input("Enter a number: "))
print(get_fibonacci_number(n))