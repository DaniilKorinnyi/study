import datetime

class MyException(Exception):
    def __init__(self, message):
        self.message = message
        self.timestamp = str(datetime.datetime.now())
        with open("error_log.txt", "a") as f:
            f.write(f"{self.timestamp}: {self.message}\n")

try:
    raise MyException("Custom exception is occured")
except MyException:
    print("Custom exception is occured")