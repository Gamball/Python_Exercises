import datetime


def main():
    try:
        # """ The variables """
        Year = datetime.datetime.now().year
        # The main
        year = int(input('inter your age:\t'.title()))
        a = Year - year
        mount = int(input('inter your birth month:\t'.title()))
        day = int(input('inter your birth day:\t'.title()))

        # """ The result """

        print('your birth data is:\n.'.title(), a, '-', mount, '-', day)
    except ValueError:
        quit('the value must be integer, please\'t!'.title())
if __name__ == '__main__': main()
