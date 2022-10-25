import pickle

from bs4 import BeautifulSoup


html = BeautifulSoup(open('resultado-mega.html'), 'html.parser')
def get_mega_sena_numbers(ls):
    FIRST = 2
    SECOND = 3
    THIRD = 4
    FOUR = 5
    FIFTY = 6
    SIXTY = 7
    return [
        ls[FIRST].string,
        ls[SECOND].string,
        ls[THIRD].string,
        ls[FOUR].string,
        ls[FIFTY].string,
        ls[SIXTY].string
    ]

table_lines = html.find('form').find_all('tbody')
ms_numbers = []
for line in table_lines:
    tr = line.tr
    if tr is None:
        continue
    columns = tr.find_all('td')
    if len(columns) < 10:
        continue
    numbers = get_mega_sena_numbers(columns)
    ms_numbers.append(numbers)

shorts_numbers = []
for i in ms_numbers:
    shorts_numbers.append(','.join(i))

with open('./msnumbers', 'wb') as file:
    pickle.dump(shorts_numbers, file)

print('end parse')