from dateutil.parser import parse

from results import fortunes
from results import numbers
import signs


def get_birthday():
    birthday_prompt = ('\nYay, let\'s get started! What is your birthday?\n\n')
    birthday_input = input(birthday_prompt)
    return parse(birthday_input)


def print_birthday_error():
    print('\nYikes, invalid birthday')


def get_magical_results(birthday):
    sign = signs.get_sign(birthday.date())
    fortune = fortunes.get_fortune()
    lucky_numbers = numbers.get_lucky_numbers()

    return {
        'fortune': fortune,
        'lucky_numbers': lucky_numbers,
        'sign': sign,
    }


def print_results(birthday, results):
    print('\nOkay, since your birthday is on {:%B %-d}'.format(birthday))
    print('... your sign is: {}'.format(results['sign'].upper()))
    print('... your horoscope for today: {}'.format(results['fortune']))
    print('... your lucky numbers are: {}'
          .format(' '.join(str(n) for n in results['lucky_numbers'])))


def main():
    try:
        birthday = get_birthday()
        results = get_magical_results(birthday)
        print_results(birthday, results)
    except ValueError:
        print_birthday_error()

    print()  # yes add another line break


if __name__ == '__main__':
    main()
