import sys

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python fibonacci.py <number>')
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        print(fibonacci(number))
    except ValueError:
        print('Please enter a valid integer.')
        sys.exit(1)