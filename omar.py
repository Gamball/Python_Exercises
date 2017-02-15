def main():

    print('-------------------------\nYou Have three tries only\n-------------------------')
    i = 1
    while i <= 3:
        q = int(input('What\'s you age?\n'))
        if q <= 15:
            print('No, Child re')
        i += 1 
        if q > 15:
            print('Teenager, Welcome')
            break

    # Another way to use if & loop statements:

    a = int(input('Type\n'))
    if a == 12:
        print('yes')
    else:
        s = 0
        while s <= 3:
            print('no')
            a = int(input('Type\n'))
            s += 1
            if a == 12:
                print('yes')
                break

if __name__ == '__main__': main()
