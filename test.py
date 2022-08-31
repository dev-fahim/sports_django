def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def op(x, y, func):
    return func(x, y)


if __name__ == '__main__':
    print(op(3, 4, mul))
