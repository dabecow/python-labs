first_multiplier = lambda m, n, x: (4 - m) / (pow(x, 1 / n) - 2)
second_multiplier = lambda m, n, x: pow(m, 2 * n) / (2 * pow(pow((x - m / 2), n), 1 / 4) + m)
solution = lambda m, n, x: first_multiplier(m, n, x) * second_multiplier(m, n, x)

if __name__ == '__main__':

    while (True):
        try:
            print("Enter the m, n, x vales")
            m = float(input("m>"))
            n = float(input("n>"))
            x = float(input("x>"))
            print("The result is: ", solution(m, n, x))
        except Exception as e:
            print(e.args[0], '\n')
