



def omar():
    x = input().split(',')
    print(x)
    print(type(x))


def func():
    i = 0
    while i < 3:
        a = int(input('--------------------------\n'
                      'What\'s solve this problem?\n'
                      '12 + 12 - 12 * 12 / 12'
                      '\n--------------------------\n'))
        if a == 12:
            print('Merci Awe')
            break
        else:
            # print('No, re')
            pass
            print('Wrong')


def main():
    func()
if __name__ == '__main__': main()
