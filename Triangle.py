def main():
    rows = int(input('inter rows:'))
    # draw normal Triangle of stars : 
    for i in range(rows):
        print(i * '*')

    # draw inverted Traingle of stars :
    for i in range(rows, 0, -1):
        print(i * '*')
if __name__ == '__main__':
    main()
