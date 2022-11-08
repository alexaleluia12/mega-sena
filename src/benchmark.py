import pickle

from commons import *
import randon_generator as rg

def countAccert(actual, guess):
    sActual = set(actual)
    sGuess = set(guess)

    return len(sActual.intersection(sGuess)) == 6

def verifyTotalHits(lines, generatorType):
    generator = generatorType()
    ns = rg.SequenceNumber()

    hits = 0
    for line in lines:
        guess = ns.create(generator)
        if countAccert(line, guess):
            hits += 1
    return hits

with open('./msnumbers', 'rb') as file:
    lines = pickle.load(file)
    lines = convert_to_list(lines)

    print('total registers', len(lines))

    hitsBF = verifyTotalHits(lines, rg.GeneratorBFLow)
    print('hits for BF', hitsBF)

    hitsAA = verifyTotalHits(lines, rg.GeneratorAALow)
    print('hits for aa', hitsAA)

    hitsPR = verifyTotalHits(lines, rg.GeneratorPureRandom)
    print('hits for pr', hitsPR)

"""
current results:
total registers 2514
hits for BF 0
hits for aa 0
hits for pr 0
"""
