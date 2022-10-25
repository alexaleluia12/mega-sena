import pickle
import pprint

"""
85 % de chance de cair um numero com mais de um digito

# primeiro digito
{1: 18.26,
 2: 17.87,
 3: 18.74,
 4: 18.63,
 5: 18.43,
 6: 3.24,
 7: 1.58,
 8: 1.7,
 9: 1.56}
 # segundo digito
{0: 11.85,
 1: 9.7,
 2: 9.77,
 3: 10.48,
 4: 10.05,
 5: 9.21,
 6: 9.64,
 7: 9.95,
 8: 9.71,
 9: 9.65}

"""

def convert_to_list(lines):
    new_lines = []
    for line in lines:
        tmp = line.split(',')
        tmp = [int(i) for i in tmp]
        new_lines.append(tmp)


    return new_lines


def count_first_digit(table):
    counts = {}
    count = 0
    for line in table:
        for number in line:
            first_digit = int(str(number)[0])
            if first_digit in counts:
                counts[first_digit] += 1
            else:
                counts[first_digit] = 1
            count += 1

    return counts, count

def count_second_digit(table):
    counts = {}
    count = 0
    for line in table:
        for number in line:
            snumber = str(number)
            if not len(snumber) > 1:
                continue
            digit = int(snumber[1])
            if digit in counts:
                counts[digit] += 1
            else:
                counts[digit] = 1
            count += 1

    return counts, count

def percentage(group, total):
    ngroup = {}
    for k, v in group.items():
        ngroup[k] = round(v/total*100, 2)

    return ngroup

with open('./msnumbers', 'rb') as file:
    lines = pickle.load(file)
    lines = convert_to_list(lines)

    first_numbers, tfirst = count_first_digit(lines)
    second_numbers, tsecond = count_second_digit(lines)

    pfirst = percentage(first_numbers, tfirst)
    psecond = percentage(second_numbers, tsecond)
    pprint.pprint(pfirst)
    pprint.pprint(psecond)