from decimal import Decimal, InvalidOperation


class UnknownOperationError(Exception):
    pass


def calculator():
    """calculator that allows you to calculate basic arithmetic operations"""
    while True:
        try:
            arithmetic_operator = input(
                "Enter arithmetic operator +, -, *, / (or 'q' to quit): "
            )
            if arithmetic_operator.lower() in "q":
                print("Calculator terminated. Goodbye!")
                break
            if arithmetic_operator not in "+-*/":
                raise UnknownOperationError(
                    f"Invalid arithmetic operator - {arithmetic_operator}"
                )
            number_one = Decimal(input("Enter the first number: "))
            number_two = Decimal(input("Enter the second number: "))
            match arithmetic_operator:
                case "+":
                    print(f"result: {number_one + number_two}")
                case "-":
                    print(f"result: {number_one - number_two}")
                case "*":
                    print(f"result: {number_one * number_two}")
                case "/":
                    print(f"result: {number_one / number_two}")
        except ValueError:
            print("Error! An incorrect number was entered.")
        except ZeroDivisionError:
            print("Error! Division by zero is impossible.")
        except UnknownOperationError as e:
            print(f"Error! {e}")
        except OverflowError:
            print("Error!  Number overflow.")
        except InvalidOperation:
            print("Error! Invalid decimal operation.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    calculator()
