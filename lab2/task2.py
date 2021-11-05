import math as m

C = lambda radius: m.pi * m.pow(radius, 2)
R = lambda side, height: side * height
P = lambda sides_count, side_length, apothem: 1 / 2 * sides_count * side_length * apothem
E = lambda : exit(0)

commands = ['C', 'R', 'P', 'E']

command_list = []
L = [['C', 'C', 'R', 'r', 'P', 'E', 'P'], [2], [1], [2, 1], [1, 2, 3], [2, 1, 1], []]

if __name__ == '__main__':

    for index, current_command in enumerate(L[0]):
        if not current_command in commands:
            continue
        arguments = "("

        for argument_index in range(0, eval(current_command + ".__code__.co_argcount")):
            arguments += str(L[index + 1][argument_index]) + ","

        arguments += ")"
        print(eval(current_command + arguments))
