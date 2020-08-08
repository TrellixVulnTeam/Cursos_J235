def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_o(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        response = fibonacci_o(n - 1, memo) + fibonacci_o (n - 2, memo)
        memo[n] = response
        print('Dictionary values:',memo)
        return response


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print('=' * 50)
    response_1 = fibonacci(n)
    print('Answer with recursive function',response_1)
    print('=' * 50)
    response_2 = fibonacci_o(n)
    print('Answer with memoizated function',response_2)
    print('=' * 50)
