from dateutil.parser import parse

from results import fortunes
from results import numbers
from tools.horoscope import signs


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

        astrological_sign = signs.get_sign(birthday)
        print('... your sign is: {}'.format(astrological_sign.upper()))

        fortune = fortunes.get_fortune()
        print('... your horoscope for today: {}'.format(fortune))

        lucky_numbers = numbers.get_lucky_numbers()
        print('... your lucky numbers are: {}'.format(' '.join(str(n) for n in lucky_numbers)))
        print('\n\n')


if __name__ == '__main__':
    main()
