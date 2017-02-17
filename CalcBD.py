
#                           ***  Still under test  ***

import datetime


def main():
    try:
        # Start Introduction
        print('- _' * 20, '''\n# welcome in omar mohammad program.
# the function of this program is calculate birth date.-- enjoy -- (:
'''.title())
        print('_ -' * 20, '''\n# All Right Reserved For:\n
https://www.facebook.com/technical.expert.omar?ref=bookmarks\n\n''', '- _' * 20)
        # End Introduction

        while True:
            # Start Variables
            a = datetime.date.today()
            year = int(input('your year:\t'))
            month = int(input('your month:\t'))
            day = int(input('your day:\t'))
            # End Variables

            '''Start Calc Days, Months & Years'''

            # ------- General ------- #
            if day > 31 or month > 12 or year > a.year or year < 1000:
                print('----------\nImpossible')
            elif (day > a.day) and (month > a.month) and (month > 5):
                print('your age is', a.year-year-1, 'years &', month-a.month, 'months &', day-a.day, 'days')
            elif (day < a.day) and (month < a.month) and (month <= 5):
                print('your age is', a.year-year, 'years &', a.month - month, 'months &', a.day - day, 'days')
            elif (day > a.day) and (month < a.month) and (month > 5):
                print('your age is', a.year - year-1, 'years &', a.month-month, 'months &', day - a.day, 'days')
            elif (day < a.day) and (month > a.month) and (month <= 5):
                print('your age is', a.year - year, 'years &', month - a.month, 'months &', a.day - day, 'days')
            elif (day < a.day) and (month > a.month) and (month > 5):
                print('your age is', a.year-year-1, 'years &', month-a.month, 'months &', a.day-day, 'days')
            elif (day > a.day) and (month < a.month) and (month <= 5):
                print('your age is', a.year - year, 'years &', a.month - month, 'months &', day - a.day, 'days')
            # ------- End General ------- #

                # ------- Days -------- #
            elif (day > a.day) and (month == a.month):
                print('your age is', a.year-year-1, 'years &', day-a.day, 'days')
            elif (day < a.day) and (month == a.month):
                print('your age is', a.year - year, 'years &', a.day - day, 'days')
                # ------- End Days -------- #

                # ------- Months -------- #
            elif (month > a.month) and (day == a.day):
                print('your age is', a.year - year-1, 'years &', month - a.month, 'months')
            elif (month < a.month) and (day == a.day):
                print('your age is', a.year - year, 'years &', a.month - month, 'months')
            elif (month > a.month) and (day == a.day):
                print('your age is', a.year-year-1, 'years &', month - a.month, 'months')
            elif (month < a.month) and (day == a.day):
                print('your age is', a.year-year, 'years &', a.month - month, 'months')
                # ------- End Months -------- #

                # if Equals
            elif (day == a.day) and (month == a.month) and (month > 5):
                print('Your age is', a.year - year - 1, 'exactly')
            elif (day == a.day) and (month == a.month) and (month <= 5):
                print('Your age is', a.year - year, 'exactly')
                # End if Equals

            else:
                print('Error')
            '''End Calc Days, Months & Years'''

            # if the user wants to re
            q = input('----------\nDo you Re? "Y"es / "N"o:\t')
            if (q == 'y') or (q == 'Y'):
                continue
            elif (q == 'n') or (q == 'N'):
                print('Merci to use')
                print('# All Right Reserved For:\n'
                      'https://www.facebook.com/technical.expert.omar?ref=bookmarks\n'
                      '.............................\n')
                break
    except ValueError:
        quit('you make mistake')
if __name__ == '__main__': main()
