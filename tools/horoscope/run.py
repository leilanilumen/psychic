from datetime import date
import random

from dateutil.parser import parse

from fortunes.fortunes import LIST_OF_FORTUNES


def main():
    birthday_prompt = ('\nYay, let\'s get started! What is your birthday?\n\n')
    birthday_input = input(birthday_prompt)
    print('')

    birthday = None
    try:
        birthday = parse(birthday_input)
    except ValueError:
        print('blah, invalid birthday')
        print('\n\n')

    if birthday:
        print('\nOkay, since your birthday is on {:%B %-d}'.format(birthday))

        astrological_sign = None
        if date(birthday.year, 3, 21) <= birthday.date() <= date(birthday.year, 4, 19):
            astrological_sign = 'aries'.upper()
        elif date(birthday.year, 4, 20) <= birthday.date() <= date(birthday.year, 5, 20):
            astrological_sign = 'taurus'.upper()
        elif date(birthday.year, 5, 21) <= birthday.date() <= date(birthday.year, 6, 20):
            astrological_sign = 'gemini'.upper()
        elif date(birthday.year, 6, 21) <= birthday.date() <= date(birthday.year, 7, 22):
            astrological_sign = 'cancer'.upper()
        elif date(birthday.year, 7, 23) <= birthday.date() <= date(birthday.year, 8, 22):
            astrological_sign = 'leo'.upper()
        elif date(birthday.year, 8, 23) <= birthday.date() <= date(birthday.year, 9, 22):
            astrological_sign = 'virgo'.upper()
        elif date(birthday.year, 9, 23) <= birthday.date() <= date(birthday.year, 10, 21):
            astrological_sign = 'libra'.upper()
        elif date(birthday.year, 10, 23) <= birthday.date() <= date(birthday.year, 11, 21):
            astrological_sign = 'scorpio'.upper()
        elif date(birthday.year, 11, 22) <= birthday.date() <= date(birthday.year, 12, 22):
            astrological_sign = 'sagittarius'.upper()
        elif (date(birthday.year - 1, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19) or
                date(birthday.year, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19)):
            astrological_sign = 'capricorn'.upper()
        elif date(birthday.year, 1, 20) <= birthday.date() <= date(birthday.year, 2, 18):
            astrological_sign = 'aquarius'.upper()
        elif date(birthday.year, 2, 19) <= birthday.date() <= date(birthday.year, 3, 20):
            astrological_sign = 'pisces'.upper()
        print('... your sign is: {}'.format(astrological_sign))

        fortune = LIST_OF_FORTUNES[random.randint(0, len(LIST_OF_FORTUNES) - 1)]
        print('... your horoscope for today: {}'.format(fortune))

        lucky_numbers = []
        for _ in range(5):
            lucky_numbers.append(random.randint(1, 99))
        lucky_numbers.sort()
        print('... your lucky numbers are: {}'.format(' '.join(str(n) for n in lucky_numbers)))
        print('\n\n')


if __name__ == '__main__':
    main()
