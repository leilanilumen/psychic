from datetime import date
import random
from dateutil.parser import parse

from crystalball import fortunes
from astrology import sings
fortune_list = [
    'You will not win the lottery, sadz',
    'You will win the lottery if you are lucky',
    'You will win the lottery if you are lucky',
    'You will win the lottery if you are lucky',
    'Be careful walking across cracks in the pavement',
    'Love will wax and wane',
    'You will win the lottery if you are lucky',
    'You will not adopt a dog',
    'A mysterious stranger will offer you a chance of a lifetime',
    'You will win the lottery if you are lucky',
    'You will win the lottery if you are lucky',
]


HELLO = "Yay, llet's get started!What is your birthday?"
def show(ln):
    print('... you\'re lucky numbers are: {}'.format(getln(ln)))
    print('\n\n')
def showbday(birhday):
    print('Okay, since your birthday is on {:%B %-d}'.format(birhday))

def getln(numbers):
    print('... you\'re lucky numbers are: {}'.format(' '.join(str(n) for n in numbers)))
    return numbers
def main():
    birthday_1 = get_the_birthday()
    print('')
    try:
        birthday = parse(birthday_1)
    except ValueError:
        print('blah, invalid birthday')
        print('\n\n')
    if birthday:
        showbday(birthday)
        tas = None
        # updated by pepper on 5/9/2016
        if date(birthday.year, 3, 21) <= birthday.date() <= date(birthday.year, 4, 19):
            tas = 'aries'.upper()
        elif date(birthday.year, 4, 20) <= birthday.date() <= date(birthday.year, 5, 20):
            tas = 'taurus'.upper()
        elif date(birthday.year, 5, 21) <= birthday.date() <= date(birthday.year, 6, 20):
            tas = 'gemini'.upper()
        elif date(birthday.year, 6, 21) <= birthday.date() <= date(birthday.year, 7, 22):
            tas = 'cancer'.upper()
        elif date(birthday.year, 7, 23) <= birthday.date() <= date(birthday.year, 8, 22):
            tas = 'leo'.upper()
        elif date(birthday.year, 8, 23) <= birthday.date() <= date(birthday.year, 9, 22):
            tas = 'virgo'.upper()
        elif date(birthday.year, 9, 23) <= birthday.date() <= date(birthday.year, 10, 21):
            tas = 'libra'.upper()
        elif date(birthday.year, 10, 23) <= birthday.date() <= date(birthday.year, 11, 21):
            tas = 'scorpio'.upper()
        elif date(birthday.year, 11, 22) <= birthday.date() <= date(birthday.year, 12, 22):
            tas = 'sagittarius'.upper()
        elif (date(birthday.year - 1, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19) or
                date(birthday.year, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19)):
            tas = 'capricorn'.upper()
        elif date(birthday.year, 1, 20) <= birthday.date() <= date(birthday.year, 2, 18):
            tas = 'aquarius'.upper()
        elif date(birthday.year, 2, 19) <= birthday.date() <= date(birthday.year, 3, 20):
            tas = 'pisces'.upper()
        # end updated on 5/9/2016
        print('..Your sign is: {}'.format(sings.generate(birthday)))
        fortune = fortunes.scry()
        print('...  your horoscope for today: {}'.format(fortune))

        ln = []
        for _ in range(5):
            ln.append(random.randint(1, 99))
        ln.sort()
        show(ln)

def get_the_birthday():
    user_birthday = None
    bday = ('\nYay, llet\'s get started!What is your birthday?\n\n')
    birthday_1 = input(bday)
    return birthday_1


if __name__ == '__main__':
    main()
