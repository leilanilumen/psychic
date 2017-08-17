from datetime import date


def get_sign(birthday):
    if date(birthday.year, 3, 21) <= birthday.date() <= date(birthday.year, 4, 19):
        return 'aries'
    elif date(birthday.year, 4, 20) <= birthday.date() <= date(birthday.year, 5, 20):
        return 'taurus'
    elif date(birthday.year, 5, 21) <= birthday.date() <= date(birthday.year, 6, 20):
        return 'gemini'
    elif date(birthday.year, 6, 21) <= birthday.date() <= date(birthday.year, 7, 22):
        return 'cancer'
    elif date(birthday.year, 7, 23) <= birthday.date() <= date(birthday.year, 8, 22):
        return 'leo'
    elif date(birthday.year, 8, 23) <= birthday.date() <= date(birthday.year, 9, 22):
        return 'virgo'
    elif date(birthday.year, 9, 23) <= birthday.date() <= date(birthday.year, 10, 21):
        return 'libra'
    elif date(birthday.year, 10, 23) <= birthday.date() <= date(birthday.year, 11, 21):
        return 'scorpio'
    elif date(birthday.year, 11, 22) <= birthday.date() <= date(birthday.year, 12, 22):
        return 'sagittarius'
    elif (date(birthday.year - 1, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19) or
            date(birthday.year, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19)):
        return 'capricorn'
    elif date(birthday.year, 1, 20) <= birthday.date() <= date(birthday.year, 2, 18):
        return 'aquarius'
    elif date(birthday.year, 2, 19) <= birthday.date() <= date(birthday.year, 3, 20):
        return 'pisces'
