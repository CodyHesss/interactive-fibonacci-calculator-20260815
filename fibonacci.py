import sys

memo = {}

def fibonacci(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise SystemExit(1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python fibonacci.py <number>')
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            print('Please enter a non-negative integer.')
            sys.exit(1)
        print(fibonacci(number))
    except ValueError:
        print('Please enter a valid integer.')
        sys.exit(1)
