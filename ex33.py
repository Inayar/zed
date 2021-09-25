i = 0
numbers = []

while i < 6:
    print(f'В начале значение  i  равно {i}')
    numbers.append(i)

    i = i + 1
    print('Текущие значения: ', numbers)
    print(f'В конце значение i равно {i}')

print('Значения: ')
for num in numbers:
    print(num)


def mmm(x):
    numbers = []

    for i in range(x):
        print(f'В начале значение i равно {i}')
        numbers.append(i)
        i += 1
        print('Текущее значение: ', numbers)
        print(f'В конце значение i равно {i}')


def mmm(x, y):
    numbers = []

    for i in range(x):
        print(f'В начале значение i равно {i}')
        numbers.append(i)
        i += y
        print('Текущее значение: ', numbers)
        print(f'В конце значение i равно {i}')
