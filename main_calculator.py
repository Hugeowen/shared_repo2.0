import calculator_operations

def main():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    if operation == 'add':
        print("Result:", calculator_operations.add(num1, num2))
    elif operation == 'subtract':
        print("Result:", calculator_operations.subtract(num1, num2))
    elif operation == 'multiply':
        print("Result:", calculator_operations.multiply(num1, num2))
    elif operation == 'divide':
        print("Result:", calculator_operations.divide(num1, num2))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
