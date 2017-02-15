

def main():
    while True:
        print('*' * 4, 'Welcome to even/odd No. Test', '*' * 4)
        a = int(input('inter No.:\t'))
        if a % 2 == 0:
            print('Your No. is even')
        else:
            print('Your No. is odd')
        b = input('Do you re? "y"es/"N"o\t')
        if b == 'n' or b == 'N':
            print('Thank you, Good by (:')
            break
        elif b == 'y' or b == 'Y':
            continue
        else:
            quit('Error')
if __name__ == '__main__':
    main()
