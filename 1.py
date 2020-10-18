string = input('Введите строку ---> ')
contains = False

if 'a' in string or 'а' in string:
    print(' A есть в строке')
else:
    print(' А нет в строке')

for char in string:
    if char == 'a' or char == 'а':
        contains = True

if contains == True:
    print(' A есть в строке')
else:
    print(' А нет в строке')
