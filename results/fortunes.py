import random

LIST_OF_FORTUNES = [
    'You will not win the lottery, sadz',
    'Be careful walking across cracks in the pavement',
    'Love will wax and wane',
    'You will not adopt a dog',
    'A mysterious stranger will offer you a chance of a lifetime'
]


def get_fortune():
    return LIST_OF_FORTUNES[random.randint(0, len(LIST_OF_FORTUNES) - 1)]
