class MyException(Exception):
   pass
try:
    raise MyException
except MyException:
    print("Custom exception is occured")


# ============================================

# class MyCustomException(Exception):
#     def __init__(self):
#         super().__init__("Custom exception is occured")
# raise MyCustomException()