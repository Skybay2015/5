import re
from string import digits
string = input('Введите строку: ')
numbers = []
letters = []

for char in string:
    if char != ' ' and char.isdigit():
        numbers.append(char)
    elif char != ' ':
        letters.append(char)

string2 = ''.join(numbers) + ''.join(letters)

print(string2)

tempN = re.findall(r'\d+', string)
tempS = re.findall(r'([a-zA-Z]+|[а-яА-Я]+)', string)

print(''.join(tempN) + ''.join(tempS))
