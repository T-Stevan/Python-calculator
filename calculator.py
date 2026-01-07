def add(a, b):
    result = a + b
    print(result)
    
def subtract(a, b):
    result = a - b
    print(result)
    
def multiply(a, b):
    result = a * b
    print(result)

def divide(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Can't divide by Zero")
    
def power(a, b):
    result = a ** b
    print(result)
    
add( 5, 7)
power(3, 2)
divide(4,0)
