import time
final_list = []


def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """
    time.sleep(.1)
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial


def sum_factorial():
    for i in range(50):
        final_list.append(factorial(i))
    result = sum(final_list)
    print("Final SUM = {}".format(result))
    return result

    
print(">>>>> checkout my new feature No 1 <<<<<")

if __name__ == "__main__":
    sum_factorial()
