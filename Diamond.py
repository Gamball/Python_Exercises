""" Draw Diamond """


def main():
    # Ask the user about how number of the row:
    rows = int(input('inter No. of rows:'))

    # # The Roll is => { i * 2 - 1 } & { rows - i}
    for i in range(rows):
        print((rows - i) * ' ', (i * 2 - 1) * '*')

    for i in range(rows, 0, -1):
        print((rows - i) * ' ', (i * 2 - 1) * '*')
if __name__ == '__main__':
    main()
