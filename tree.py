

""" Draw Tree """


def main():
    # Ask the user about how number of the row:
    rows = int(input('inter No. of rows:'))

    # # The Roll is => { i * 2 - 1 } & { rows - i}
    for i in range(rows):
        print((rows - i) * ' ', (i * 2 - 1) * '*')

    for i in range(rows // 2, rows):
        print((rows - i) * ' ', (i * 2 - 1) * '*')

    for i in range(3):
        print((rows - 2) * ' ', '||')
if __name__ == '__main__':
    main()
