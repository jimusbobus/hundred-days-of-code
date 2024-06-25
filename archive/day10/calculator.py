import helper


def add(n1, n2):
    """Add the two numbers passed in"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract the two numbers passed in"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply the two numbers passed in"""
    return n1 * n2


def divide(n1, n2):
    """Divide the two numbers passed in"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(helper.logo)
    number1 = float(input("What is the first number: "))
    for symbol in operations:
        print(symbol)
    while True:
        operation = input("Choose an operation: ")
        next_number = float(input("What's the next number: "))
        answer = operations[operation](number1, next_number)

        print(f"{number1} {operation} {next_number} = {answer}")

        more_operations = input(
            "Choose an option: \n'y' = perform another operation on this calculation, "
            "'n' = start a new calculation, any other input ends the program.")
        if more_operations == "y":
            number1 = answer
        elif more_operations == "n":
            print(helper.clear_screen())
            calculator()
            break
        else:
            break


calculator()
