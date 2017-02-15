""" Python program """


def omar():
    file = open('c:\\users\omar\desktop\welcome.php', 'w')
    file.write('welcome men in Php language')
    try:
        file = open('c:\\users\omar\desktop\welcome.php', 'r')
        for i in file:
            print(i)
        file.close()
    except IOError:
        print('You make mistake')


def main():
    omar()
if __name__ == '__main__': main()
