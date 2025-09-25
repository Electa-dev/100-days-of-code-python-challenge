def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    import art
    print(art.logo)
    print("Welcome to the calculator!!!")

    first_num = int(input("Enter your first number here: "))
    calculate = False
    while not calculate:
        symbol = input("Pick a symbol:\n+\n-\n/\n*\nEnter symbol here: ")
        second_num = int(input("Enter your second number: "))
        result = operations[symbol] (first_num, second_num)
        print(f"{first_num} {symbol} {second_num} = {result}")

        continue_calculation = input("Continue calculation with number? 'y' for yes or 'n' to start new calculation and to stop 'e': ").lower()
        if continue_calculation == 'y':
            first_num = result
        elif continue_calculation == "n":
            calculate = True
            print("\n" * 100)
            calculator()
        elif continue_calculation == "e":
            calculate = True
            print("Goodbye")
        else:
            print("Enter the right input!!!")
            calculator()


calculator()




