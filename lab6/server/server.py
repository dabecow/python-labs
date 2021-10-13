import socket

IP_ADDRESS = "127.0.0.1"
PORT = 8103
BUFFER_SIZE = 1024


def applyOp(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b


def evaluate(expression):
    values = []

    operators = []
    i = 0

    while i < len(expression):

        if expression[i] == ' ':
            i += 1
            continue

        elif expression[i].isdigit():
            val = ''

            while i < len(expression) and expression[i].isdigit():
                val += expression[i]
                i += 1

            values.append(int(val, 2))

            i -= 1

        else:

            while len(operators) != 0:
                val2 = values.pop()
                val1 = values.pop()
                op = operators.pop()

                values.append(applyOp(val1, val2, op))

            operators.append(expression[i])

        i += 1

    while len(operators) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = operators.pop()

        values.append(applyOp(val1, val2, op))

    return values[-1]


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        socket.bind((IP_ADDRESS, PORT))
        socket.listen(1)
        connection, address = socket.accept()
        with connection:
            print('Connected by', address)
            while True:
                data = connection.recv(BUFFER_SIZE)
                if data.__str__() == '':
                    connection.sendall('Error'.encode())
                    break

                try:
                    result = evaluate(data.decode())
                    connection.sendall(str(result).encode())
                except Exception as e:
                    connection.sendall('Error'.encode())
