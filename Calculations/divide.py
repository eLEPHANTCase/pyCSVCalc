def divisiondecor8r(method):
    def check_division(a, b):
        if b == 0:
            print("Cannot divide by zero!")
            return
        return method(a, b)

@divisiondecor8r
def division(a, b):
    return float(a) / float(b