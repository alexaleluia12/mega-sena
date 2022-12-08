import pickle
import time
import random

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

def multiplyHits(hits):
    points = 0
    tableMultiples = {
        1: 0.01,
        2: 0.2,
        3: 0.5,
        4: 15,
        5: 90,
        6: 1000
    }
    for i in range(1, 7):
        points += hits.get(i, 0) * tableMultiples[i]

    return points

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

def fitnessMany():
    with open('./msnumbers', 'rb') as file:
        lines = pickle.load(file)
        lines = convert_to_list(lines)

        print('total registers', len(lines))
        bests = []
        for _ in range(1, len(lines)):
            i = 3000 + random.randint(100, 1000)
            hitsAA = verifyGroupsOfHits(lines, rg.GeneratorAALow)
            score = multiplyHits(hitsAA)

            bests.append(score)
            print(score)
        print()
        print(sum(bests) / len(bests), '+')

def fitness():
    with open('./msnumbers', 'rb') as file:
        lines = pickle.load(file)
        lines = convert_to_list(lines)

        print('total registers', len(lines))

        i = 1000 + random.randint(100, 1000)
        hitsAA = verifyGroupsOfHits(lines, rg.GeneratorAALow, i)
        score = multiplyHits(hitsAA)
        d = {
            "h": hitsAA,
            "seed": i,
            "score": score
        }
        print('seed', d["seed"], 'score', d['score'])
        printTableResults(d["h"], 'aa')
