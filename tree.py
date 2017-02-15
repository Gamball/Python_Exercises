

def main():
    a = list(range(1, 6))
    a.sort(reverse=True)
    for o in a:
        print(o)

    for z in range(1, 6):
        a = list(range(1, 6))
        a.sort(reverse=True)
        print(z * '*', * '*')
if __name__ == '__main__':
    main()