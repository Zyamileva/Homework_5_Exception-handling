from pathlib import Path
from decimal import Decimal, InvalidOperation


def file_calculate_average(numberplate: Path):
    """Calculates the average"""
    try:
        with numberplate.open("r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("The file is empty.")
            numbers = []
            for line in lines:
                try:
                    numbers.extend(map(Decimal, line.split()))
                except ValueError:
                    print("The file contains non-numeric value")
                    return None
            return sum(numbers) / len(numbers)
    except FileNotFoundError:
        print("Error: File not found.")
    except InvalidOperation:
        print("Error! Invalid decimal operation.")
    except Exception as e:
        print(f"Error: {e}")
    return None


fileName = Path("number.txt")
if __name__ == "__main__":
    average = file_calculate_average(fileName)
    if average is not None:
        print(f"Arithmetic average: {average}")
