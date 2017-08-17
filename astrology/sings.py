from datetime import date


def _generate(birthday):
    mysign = None
    if date(birthday.year, 3, 21) <= birthday.date() <= date(birthday.year, 4, 19):
        mysign = 'aries'.upper()
    elif date(birthday.year, 4, 20) <= birthday.date() <= date(birthday.year, 5, 21):
        mysign = 'taurus'.upper()
    elif date(birthday.year, 5, 21) <= birthday.date() <= date(birthday.year, 6, 22):
        mysign = 'gemini'.upper()
    elif date(birthday.year, 6, 21) <= birthday.date() <= date(birthday.year, 7, 21):
        mysign = 'cancer'.upper()
    elif date(birthday.year, 7, 23) <= birthday.date() <= date(birthday.year, 8, 21):
        mysign = 'leo'.upper()
    elif date(birthday.year, 8, 23) <= birthday.date() <= date(birthday.year, 9, 22):
        mysign = 'virgo'.upper()
    elif date(birthday.year, 9, 23) <= birthday.date() <= date(birthday.year, 10, 21):
        mysign = 'libra'.upper()
    elif date(birthday.year, 10, 23) <= birthday.date() <= date(birthday.year, 11, 21):
        mysign = 'scorpio'.upper()
    elif date(birthday.year, 11, 22) <= birthday.date() <= date(birthday.year, 12, 22):
        mysign = 'sagittarius'.upper()
    elif (date(birthday.year - 1, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19) or
            date(birthday.year, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19)):
        mysign = 'capricorn'.upper()
    elif date(birthday.year, 1, 20) <= birthday.date() <= date(birthday.year, 2, 18):
        mysign = 'aquarius'.upper()
    elif date(birthday.year, 2, 19) <= birthday.date() <= date(birthday.year, 3, 20):
        mysign = 'pisces'.upper()
    return mysign

    # def generate(birthday):
    #     astrological_sign = None
    #     if date(birthday.year, 3, 21) <= birthday.date() <= date(birthday.year, 4, 19):
    #         astrological_sign = 'aries'.upper()
    #     elif date(birthday.year, 4, 20) <= birthday.date() <= date(birthday.year, 5, 20):
    #         astrological_sign = 'taurus'.upper()
    #     elif date(birthday.year, 5, 21) <= birthday.date() <= date(birthday.year, 6, 20):
    #         astrological_sign = 'gemini'.upper()
    #     elif date(birthday.year, 6, 21) <= birthday.date() <= date(birthday.year, 7, 22):
    #         astrological_sign = 'cancer'.upper()
    #     elif date(birthday.year, 7, 23) <= birthday.date() <= date(birthday.year, 8, 22):
    #         astrological_sign = 'leo'.upper()
    #     elif date(birthday.year, 8, 23) <= birthday.date() <= date(birthday.year, 9, 22):
    #         astrological_sign = 'virgo'.upper()
    #     elif date(birthday.year, 9, 23) <= birthday.date() <= date(birthday.year, 10, 21):
    #         astrological_sign = 'libra'.upper()
    #     elif date(birthday.year, 10, 23) <= birthday.date() <= date(birthday.year, 11, 21):
    #         astrological_sign = 'scorpio'.upper()
    #     elif date(birthday.year, 11, 22) <= birthday.date() <= date(birthday.year, 12, 22):
    #         astrological_sign = 'sagittarius'.upper()
    #     elif (date(birthday.year - 1, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19) or
    #             date(birthday.year, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19)):
    #         astrological_sign = 'capricorn'.upper()
    #     elif date(birthday.year, 1, 20) <= birthday.date() <= date(birthday.year, 2, 18):
    #         astrological_sign = 'aquarius'.upper()
    #     elif date(birthday.year, 2, 19) <= birthday.date() <= date(birthday.year, 3, 20):
    #         astrological_sign = 'pisces'.upper()
    #     return astrological_sign

def generate(birthday): # PSYCHIC WANTED TO CHANGE TO 13-SIGN ZODIAC
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
        #astrological_sign = 'libra'
    elif date(birthday.year, 9, 23) <= birthday.date() <= date(birthday.year, 10, 21):
        astrological_sign = 'libra'.upper()
    elif date(birthday.year, 10, 23) <= birthday.date() <= date(birthday.year, 11, 21):
        astrological_sign = 'scorpio'.upper()
        #astrological_sign = 'ophiucus'
    elif date(birthday.year, 11, 22) <= birthday.date() <= date(birthday.year, 12, 22):
        astrological_sign = 'sagittarius'.upper()
    elif (date(birthday.year - 1, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19) or
            date(birthday.year, 12, 22) <= birthday.date() <= date(birthday.year + 1, 1, 19)):
        # astrological_sign = 'cappricorn'.upper()
        astrological_sign = 'capricorn'.upper()
    elif date(birthday.year, 1, 20) <= birthday.date() <= date(birthday.year, 2, 18):
        astrological_sign = 'aquarius'.upper()
    elif date(birthday.year, 2, 19) <= birthday.date() <= date(birthday.year, 3, 20):
        astrological_sign = 'pisces'.upper()
    return astrological_sign
