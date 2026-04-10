class Calculator:
    def __init__(self):
        self.history = []
        self.max_history = 10
        self.last_result = 0

    def add(self, a, b):
        result = a + b
        self.last_result = result
        self._record_calculation(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.last_result = result
        self._record_calculation(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.last_result = result
        self._record_calculation(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.last_result = result
        self._record_calculation(f"{a} / {b}", result)
        return result

    def _record_calculation(self, operation, result):
        entry = {"operation": operation, "result": result}
        self.history.append(entry)
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def view_history(self):
        if not self.history:
            return "No calculation history available."
        
        history_text = "\n" + "=" * 50 + "\n"
        history_text += "CALCULATION HISTORY (Last 10)\n"
        history_text += "=" * 50 + "\n"
        
        for index, entry in enumerate(self.history, 1):
            history_text += f"{index}. {entry['operation']} = {entry['result']}\n"
        
        history_text += "=" * 50 + "\n"
        return history_text

    def clear_history(self):
        self.history = []
        self.last_result = 0
        return "Calculator history and state cleared."

    def get_last_result(self):
        return self.last_result


def main():
    calc = Calculator()
    
    print("\n" + "=" * 50)
    print("MINIMALIST CALCULATOR")
    print("=" * 50)
    print("Commands:")
    print("  add <a> <b>      - Add two numbers")
    print("  sub <a> <b>      - Subtract two numbers")
    print("  mul <a> <b>      - Multiply two numbers")
    print("  div <a> <b>      - Divide two numbers")
    print("  history          - View calculation history")
    print("  clear            - Clear history and reset")
    print("  quit             - Exit calculator")
    print("=" * 50 + "\n")
    
    while True:
        try:
            user_input = input("Enter command: ").strip().lower()
            
            if not user_input:
                continue
            
            parts = user_input.split()
            command = parts[0]
            
            if command == "quit":
                print("\nGoodbye!\n")
                break
            
            elif command == "history":
                print(calc.view_history())
            
            elif command == "clear":
                message = calc.clear_history()
                print(f"\n{message}\n")
            
            elif command == "add":
                if len(parts) < 3:
                    print("Usage: add <number1> <number2>\n")
                    continue
                a, b = float(parts[1]), float(parts[2])
                result = calc.add(a, b)
                print(f"Result: {result}\n")
            
            elif command == "sub":
                if len(parts) < 3:
                    print("Usage: sub <number1> <number2>\n")
                    continue
                a, b = float(parts[1]), float(parts[2])
                result = calc.subtract(a, b)
                print(f"Result: {result}\n")
            
            elif command == "mul":
                if len(parts) < 3:
                    print("Usage: mul <number1> <number2>\n")
                    continue
                a, b = float(parts[1]), float(parts[2])
                result = calc.multiply(a, b)
                print(f"Result: {result}\n")
            
            elif command == "div":
                if len(parts) < 3:
                    print("Usage: div <number1> <number2>\n")
                    continue
                a, b = float(parts[1]), float(parts[2])
                result = calc.divide(a, b)
                print(f"Result: {result}\n")
            
            else:
                print("Unknown command. Please try again.\n")
        
        except ValueError as e:
            print(f"Error: {e}\n")
        except IndexError:
            print("Invalid input format. Please check your command.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")


if __name__ == "__main__":
    main()
