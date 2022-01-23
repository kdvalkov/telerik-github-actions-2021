import time
final_list = []


def factorial(n):
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


if __name__ == "__main__":
    sum_factorial()
