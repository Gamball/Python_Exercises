def main():
    try:
        print('Remember, You have 3 tries only, Go ahead\n')
        w = 0
        while w < 3:
            w += 1
            a = '100'
            b = '101'
            c = '150'
            d = '0'
            question = input('what\'s a boil degrees for water?\nA)' + a + '\nB)' + b + '\nC)' + c + '\nD)' + d + '\n')
            if question == 'A' or question == 'a' or question == a:
                print('True, Logical answer')
                break
            else: print('Error')
            continue
    except NameError:
        quit('Your are Stupid')
if __name__ == '__main__':
    main()
