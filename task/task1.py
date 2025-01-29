from decimal import Decimal


class UnknownOperationError(Exception):
    pass


def calculator():
    while True:
        try:
            arithmetic_operator = input("Enter arithmetic operator +, -, *, /: ")
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
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    calculator()
