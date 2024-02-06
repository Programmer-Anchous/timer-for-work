def move(y, x):
    print("\033[{};{}H".format(y, x))


def clear():
    print(chr(27) + "[2J")
    move(0, 0)
