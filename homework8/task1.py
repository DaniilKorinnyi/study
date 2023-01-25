from datetime import datetime


def decorator(func):
  def wrap():
    print(func.__name__ + " was called at " + str(datetime.now()))
    return func()
  return wrap
@decorator
def func1():
  pass
@decorator
def func2():
  pass
func1()
func2()