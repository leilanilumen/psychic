import random


LOWEST_LUCKY_NUMBER = 1
HIGHEST_LUCKY_NUMBER = 99


def get_lucky_numbers(size=5):
    lucky_numbers = []
    for _ in range(size):
        lucky_numbers.append(random.randint(LOWEST_LUCKY_NUMBER, HIGHEST_LUCKY_NUMBER))

    lucky_numbers.sort()
    return lucky_numbers
