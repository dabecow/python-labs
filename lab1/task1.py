import math as m


def first_multiplier(m, n, x):
    if n == 0:
        raise ValueError("Wrong value: the n can't be 0")

    denominator = (pow(x, 1 / n) - 2)
    if denominator == 0:
        raise ValueError("Wrong value: the first multiplier's denominator is 0")
    return (4 - m) / denominator


def second_multiplier(m, n, x):
    inner_expression = pow((x - m / 2), n)

    if inner_expression < 0:
        raise ValueError("Can't find even square root of the negative value")

    denominator = pow(inner_expression, 1 / 4) + m

    if (denominator < 0):
        raise ValueError("Wrong value: the second multiplier's denominator is 0")

    return pow(m, 2 * n) / (2 * denominator)


def solution(m, n, x):
    return first_multiplier(m, n, x) * second_multiplier(m, n, x)


if __name__ == '__main__':

    while (True):
        try:
            print("Enter the m, n, x vales")
            m = float(input("m>"))
            n = float(input("n>"))
            x = float(input("x>"))
            print("The result is: ", solution(m, n, x))
        except ValueError as err:
            print(err.args[0], '\n')
