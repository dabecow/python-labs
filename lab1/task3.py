import math as m


def circle(radius):
    if radius <= 0:
        raise ValueError("Wrong value")

    return m.pi * m.pow(radius, 2)


def rhombus(side, height):
    if side <= 0 or height <= 0:
        raise ValueError("Wrong value")

    return side * height


def polygon(sides_count, side_length, apothem):
    if sides_count <= 0 or side_length <= 0 or apothem <= 0:
        raise ValueError("Wrong values")

    p = sides_count * side_length
    return 1 / 2 * p * apothem


if __name__ == '__main__':
    choice = str()

    while True:
        choice = str(input("C – circle\nR – rhombus\nP - polygon\nE - exit\n>"))
        try:
            if choice == "C":
                print(circle(float(input("Enter the radius\n>"))))
            elif choice == "R":
                print(rhombus(
                    float(input("Enter the side's value\n>")),
                    float(input("Enter the height's value\n>"))
                ))
            elif choice == "P":
                print(polygon(
                    float(input("Enter the sides count\n>")),
                    float(input("Enter the side's length\n>")),
                    float(input("Enter the apothegm's length value\n>")),
                ))
            elif choice == "E":
                exit(0)
            else:
                raise ValueError("Wrong value\n")
        except Exception as e:
            print(e.args[0])
