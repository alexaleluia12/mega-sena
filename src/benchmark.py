import pickle
from unittest import result

from commons import *
import randon_generator as rg

def countAccert(actual, guess):
    sActual = set(actual)
    sGuess = set(guess)

    return len(sActual.intersection(sGuess)) == 6

def countAmountAccerts(actual, guess):
    sActual = set(actual)
    sGuess = set(guess)

    return len(sActual.intersection(sGuess))


def verifyTotalHits(lines, generatorType):
    generator = generatorType()
    ns = rg.SequenceNumber()

    hits = 0
    for line in lines:
        guess = ns.create(generator)
        if countAccert(line, guess):
            hits += 1
    return hits

def verifyGroupsOfHits(lines, generatorType):
    generator = generatorType()
    ns = rg.SequenceNumber()

    hits = {}
    for line in lines:
        guess = ns.create(generator)
        count = countAmountAccerts(line, guess)
        if count in hits:
            hits[count] += 1
        else:
            hits[count] = 1

    return hits

def allWin():
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

def printTableResults(results, name):
    print(name)
    for i in range(6, 0, -1):
        print(i, results.get(i, 0))
    print('-'*10)

def hits():
    print('hits\n\n')
    with open('./msnumbers', 'rb') as file:
        lines = pickle.load(file)
        lines = convert_to_list(lines)

        print('total registers', len(lines))

        hitsBF = verifyGroupsOfHits(lines, rg.GeneratorBFLow)
        printTableResults(hitsBF, 'bf')

        hitsAA = verifyGroupsOfHits(lines, rg.GeneratorAALow)
        printTableResults(hitsAA, 'aa')

        hitsPR = verifyGroupsOfHits(lines, rg.GeneratorPureRandom)
        printTableResults(hitsPR, 'pr')

hits()

"""
current results (allWin):
total registers 2514
hits for BF 0
hits for aa 0
hits for pr 0
"""
