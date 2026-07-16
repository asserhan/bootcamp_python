import sys


def calcule():
    args = sys.argv[1:]

    if not args:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n    python operations.py 10 3")
        return

    if len(args) > 2:
        print("AssertionError: too many arguments")
        return

    if len(args) < 2:
        print("AssertionError: too few arguments")
        return

    try:
        a = int(args[0])
        b = int(args[1])
    except ValueError:
        print("AssertionError: only integers")
        return

    print(f"Sum:         {a + b}")
    print(f"Difference:  {a - b}")
    print(f"Product:     {a * b}")

    try:
        print(f"Quotient:    {a / b}")
    except ZeroDivisionError:
        print("Quotient:    ERROR (division by zero)")

    try:
        print(f"Remainder:   {a % b}")
    except ZeroDivisionError:
        print("Remainder:   ERROR (modulo by zero)")


if __name__ == "__main__":
    calcule()