def factorial(n):
    #n! can also be defined as n * (n-1)!
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        #print(n / 0)
        return n * factorial(n-1)


try:
    print(factorial(1000))
except (RecursionError, OverflowError):
    print("This Program can not calculate factorials that large")
# except ZeroDivisionError:
#     print("There is a Zero Division error at line 7")

print("Program terminating")

