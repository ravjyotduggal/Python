import sys

try:
    i = int(input("Please enter the first number "))
    j = int(input("Please enter the second number "))
except (EOFError, ValueError):
    sys.exit(0)
else:
    print("Numbers are int")
finally:
    print("The finally clause will always executes")


def div(a, b):
    try:
        return int(a)//int(b)
    except (ValueError, ZeroDivisionError, EOFError):
        print("There is an issue in the programme")
        exit()


print(div(i, j))
