def main():
    print("Simple Calculator")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation = get_operation()

        if operation == 'add':
            result = calculator_operations.add(num1, num2)
        elif operation == 'subtract':
            result = calculator_operations.subtract(num1, num2)
        elif operation == 'multiply':
            result = calculator_operations.multiply(num1, num2)
        elif operation == 'divide':
            result = calculator_operations.divide(num1, num2)
        elif operation == 'square_root':
            result = calculator_operations.square_root(num1)
        elif operation == 'absolute_value':
            result = calculator_operations.absolute_value(num1)
        elif operation == 'quadratic':
            result = calculator_operations.quadratic(num1)

        print("Result:", result)
        
        if input("Do another calculation? (yes/no): ").lower() != 'yes':
            return result  # 返回最后一个计算结果并退出

if __name__ == "__main__":
    final_result = main()
    print("Final Result:", final_result)
