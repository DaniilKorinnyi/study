try:
    print("==========")
    print("This code will be executed")
    x = 1 / 0
    print("This code will not be executed")
except Exception as e:
    print("==========")
    print(f"Error occured: {e}")
else:
    print("==========")
finally:
    print("==========")
    print("This code will always be executed")