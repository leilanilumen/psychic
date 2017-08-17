import random

flist = [
    'You will not win theLotterey, sadz',
    'You will win the lotttery if you are lucky',
    'You will win the lottetry if you are lucky',
    'You will win the lottereey if you are lucky',
    'Be careful walking across cracks in the pavement',
    'Love will wax and wane',
    'You will win theLotterey if you are lucky',
    'You will not adopt a dog',
    'A mysterious stranger will offer you a chance of a lifetime',
    'You will win theLotterey if you are lucky',
    'You will win theLotterey if you are lucky',
    'You will win theLotterey if you are lucky',
    'You will win theLotterey if you are lucky',
    'You will win theLotterey if you are lucky',
    'You will win theLotterey if you are lucky',
    'You will win theLotterey if you are lucky',
    'You will win theLotterey if you are lucky',
]

# returns a random fortune from the list
def scry():
    return flist[random.randint(0, len(flist) - 1)]
