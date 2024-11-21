def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": divide
}

def calculator():
    should_continue = True
    while should_continue:
        try:
            first_number = float(input("What is the first number? "))
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation from the line above: ")
            second_number = float(input("What's the second number? "))

            calculation_function = operations[operation_symbol]
            answer = calculation_function(first_number, second_number)

            print(f"{first_number} {operation_symbol} {second_number} = {answer}")

            user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
            if user_choice == 'y':
                first_number = answer
            else:
                should_continue = False
        except ValueError:
            print("Invalid input. Please enter a number.")

calculator()