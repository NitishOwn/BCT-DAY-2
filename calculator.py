def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error."
    return a / b

while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice == '5':
        print("Thank you")
        break 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", sub(num1, num2))
    elif choice == '3':
        print("Result:", mul(num1, num2))
    elif choice == '4':
        print("Result:", div(num1, num2))
    else:
        print("Invalid choice! Please enter a valid option.")
