import datetime
def decorator(func):
    def wrapper(*args, **kwargs):
        with open('addition', 'a') as f:
            f.write(f'{func.__name__} was called at {datetime.datetime.now()}\n')
        return func(*args, **kwargs)
    return wrapper
@decorator
def add(a, b):
    return a + b
@decorator
def sub(a, b):
    return a - b
add(1, 2)
sub(1, 2)