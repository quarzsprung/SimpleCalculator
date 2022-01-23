
def calculate():
    number1 = float(input("Geben Sie die erste Zahl ein: "))
    number2 = float(input("Geben Sie die zweite Zahl ein: "))
    operator = input("Geben Sie den Rechenoperator ein: ")

    if operator == "+":
        return print(number1 + number2)
    elif operator == "-":
        return print(number1 - number2)
    elif operator == "/":
        return print(number1 / number2)
    elif operator == "*":
        return print(number1 * number2)
    else:
        print("Ungültiger Operator!")


if __name__ == '__main__':

    calculate()





