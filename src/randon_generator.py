import random


def can_append(to_check, list):
    if to_check not in list and to_check <= 60:
        return True
    return False

class GeneratorPureRandom():
    def prandom(self):
        return random.randint(1, 60)

    def two_digits(self, chosen):
        digit = self.prandom()
        if can_append(digit, chosen):
            chosen.append(digit)
            return True
        return False

    def one_digit(self, chosen):
        digit = self.prandom()
        if can_append(digit, chosen):
            chosen.append(digit)
            return True
        return False

class GeneratorBFLow():
    def __init__(self) -> None:
        self.population_two_digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.weights_two_digit = [0.118, 0.09, 0.09, 0.104, 0.10, 0.092, 0.096, 0.099, 0.097, 0.096]

    def chose_one_digit(self):
        population = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #Specify the weights
        #these are the Benford Law weights)
        weights = [0.301, 0.176, 0.124, 0.096, 0.079, 0.066, 0.057, 0.054, 0.047]
        #generate sample first_digit set with Benford disctibution
        #k = 10**6 generates 1 million values
        first_digits = random.choices(population, weights, k=1)

        return first_digits[0]

    def chose_second_digit(self):
        random_number = random.choices(self.population_two_digit, self.weights_two_digit, k=1)
        return random_number[0]

    def two_digits(self, chosen):
        d1 = self.chose_one_digit()
        d2 = self.chose_second_digit()
        digit = int(str(d1) + str(d2))
        if can_append(digit, chosen):
            chosen.append(digit)
            return True
        return False

    def one_digit(self, chosen):
        digit = self.chose_one_digit()
        if can_append(digit, chosen):
            chosen.append(digit)
            return True
        return False

class GeneratorAALow():
    def __init__(self) -> None:
        self.population_one_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.weights_one_digit = [0.182, 0.179, 0.17, 0.186, 0.184, 0.032, 0.0150, 0.017, 0.015]
        self.population_two_digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.weights_two_digit = [0.118, 0.09, 0.09, 0.104, 0.10, 0.092, 0.096, 0.099, 0.097, 0.096]

    def chose_one_digit(self):
        random_number = random.choices(self.population_one_digit, self.weights_one_digit, k=1)
        return random_number[0]

    def chose_second_digit(self):
        random_number = random.choices(self.population_two_digit, self.weights_two_digit, k=1)
        return random_number[0]

    def two_digits(self, chosen):
        d1 = self.chose_one_digit()
        d2 = self.chose_second_digit()
        digit = int(str(d1) + str(d2))
        if can_append(digit, chosen):
            chosen.append(digit)
            return True
        return False

    def one_digit(self, chosen):
        digit = self.chose_one_digit()
        if can_append(digit, chosen):
            chosen.append(digit)
            return True
        return False

class SequenceNumber:
    def __init__(self, amount=6) -> None:
        self.chosen = []
        self.PERCENT_TWO_DIGITS = 0.85
        self.amount = amount

    def create(self, gen):
        for _ in range(self.amount):
            r = random.random()

            if r <= self.PERCENT_TWO_DIGITS:
                was_sucessfull = gen.two_digits(self.chosen)
                while not was_sucessfull:
                    was_sucessfull = gen.two_digits(self.chosen)
            else:
                was_sucessfull = gen.one_digit(self.chosen)
                while not was_sucessfull:
                    was_sucessfull = gen.one_digit(self.chosen)

        self.chosen.sort()
        cp = self.chosen.copy()
        self.chosen = []
        return cp
