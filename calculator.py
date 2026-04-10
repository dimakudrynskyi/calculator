def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot perform modulo with zero")
    return a % b


OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulo
}


def parse_input(user_input):
    parts = user_input.strip().split()
    
    if len(parts) != 3:
        raise ValueError("Invalid format. Use: number operator number")
    
    try:
        first_number = float(parts[0])
        operator = parts[1]
        second_number = float(parts[2])
    except ValueError:
        raise ValueError("Numbers must be valid integers or decimals")
    
    if operator not in OPERATIONS:
        valid_ops = ', '.join(OPERATIONS.keys())
        raise ValueError(f"Invalid operator '{operator}'. Valid operators: {valid_ops}")
    
    return first_number, operator, second_number


def calculate(first_number, operator, second_number):
    operation = OPERATIONS[operator]
    return operation(first_number, second_number)


def display_welcome():
    print("\n" + "="*50)
    print("Welcome to the Minimalist Calculator")
    print("="*50)
    print("\nSupported operations: + - * / ** %")
    print("Format: number operator number")
    print("Example: 10 + 5")
    print("Type 'quit' to exit\n")


def display_result(first_number, operator, second_number, result):
    print(f"\n{first_number} {operator} {second_number} = {result}")


def run_calculator():
    display_welcome()
    
    while True:
        user_input = input("Enter calculation: ").strip()
        
        if user_input.lower() == 'quit':
            print("\nThank you for using the calculator. Goodbye!\n")
            break
        
        if not user_input:
            print("Error: Please enter a calculation.")
            continue
        
        try:
            first_number, operator, second_number = parse_input(user_input)
            result = calculate(first_number, operator, second_number)
            display_result(first_number, operator, second_number, result)
        
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    run_calculator()
