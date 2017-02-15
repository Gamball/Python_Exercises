import datetime


def trial():

    try:  # بمعنى حاول تنفذه
        read = open('C:\\Users\omar\Desktop\\non.txt', 'r')
        for line in read:
            print(line)
        read.close()

    except IOError:  # بمعنى لو لم يتم تنفيذه لوجود خطأإطبع التالي
        quit('File not found')


def name():
    try:
        nod = open('name.py', 'r')
        for ned in nod:
            print(ned)
        nod.close()

    except IOError:
        quit('You Have Error')


def main():

    trial()
    name()
if __name__ == '__main__': main()