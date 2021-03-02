@divisiondecor8r
def divide(a, b):
    try:
        a/b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return
