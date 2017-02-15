
def add():
    print('Welcome to Add:')
    a = input('inter numbers:\n').split(',')
    z = []
    for i in a:
        z.append(int(i))
    print(sum(z))


def multiplied_by():
    print('Welcome to Multiplied by:')
    a = input('inter numbers:\n')
    a = [int(x) for x in a.split(',')]
    z = 1
    for n in a:
        z *= n
    print(z)


def main():
    print('welcome men in calculator\nchoose:\n1) (add)\n2) (multiplied by)\n-----------------')
    b = int(input())
    if b == 1:
        add()
    elif b == 2:
        multiplied_by()
    else:
        print('False')


if __name__ == '__main__': main()
