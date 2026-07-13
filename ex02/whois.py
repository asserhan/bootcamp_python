import sys

try:
    if len(sys.argv[1:]) > 1:
        raise AssertionError("more than one argument is provided")
    
    if len(sys.argv[1:]) == 0:
        sys.exit()

    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print('AssertionError: argument is not an integer')