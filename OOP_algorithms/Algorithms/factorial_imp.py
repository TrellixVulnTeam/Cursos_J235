import time
import sys


def factorial_n(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response


def factorial_r(n):

    if n == 1:
        return 1

    return n * factorial_r(n - 1)


def main():
    x = int(input('Type a number: '))

    sys.setrecursionlimit(500000)

    start = time.time()
    factorial_n(x)
    end = time.time()
    print('Normal',end - start)

    start = time.time()
    factorial_r(x)
    end = time.time()
    print('Recursive',end - start)


if __name__ == '__main__':
    main()
