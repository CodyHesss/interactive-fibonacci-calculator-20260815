import sys

memo = {0: 0, 1: 1}

def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Input must be a non-negative integer')
    if n == 0:
        memo.clear()
        memo.update({0: 0, 1: 1})
        return 0
    if n not in memo:
        for index in range(max(memo) + 1, n + 1):
            memo[index] = memo[index - 1] + memo[index - 2]
    return memo[n]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python fibonacci.py <number>')
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        print(fibonacci(number))
    except ValueError as e:
        print(e)
        sys.exit(1)
