def add(a, b):
    result = a + b
    return result
    
def subtract(a, b):
    result = a - b
    return result
    
def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Can't divide by Zero")
    
def power(a, b):
    result = a ** b
    return result
    
while True:
    print("----Menu: ----")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exponential")
    print("6: Exit calculator")

    choice = input(" Choose one option from (1-6)")
    if choice == "6":
        print("---Power off----") 
        break
    
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid option, try again")
        continue
    
    num1 = int(input("Enter first number: \n"))
    num2 = int(input("Enter second number: \n"))
    
    if choice == "1":
        print("Result: ", add(num1, num2) )
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result: ", divide(num1, num2))
    elif choice == "5":
        print("Result: ", power(num1, num2))
    elif choice == "6":
        print("---Power off----") 
        break
    

