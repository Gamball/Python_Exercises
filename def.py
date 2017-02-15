import datetime


def main():
    try:
        print(datetime.datetime.now().date())
    except ImportError:
        print('Error')

    try:
        print('omar')
    except (NameError, SyntaxError):
        print('You make mistake')
    finally:
        print('Hey!')
    try:
        for i in range(5):
            print('hi')
    except NameError:
            print ('Error in the name')
    try:
        a = 7
        b = 0
        print(a / b)
    except ZeroDivisionError:
        print('كمية غير معرفة')
if __name__ == '__main__': main()
