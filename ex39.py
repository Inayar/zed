# схема связей аббревеатур с названиями стран
stses = {
    'Россия': 'RU',
    'Германия': 'DE',
    'Узбекистан': 'UZ',
    'Зимбабве': 'ZW',
    'Турция': 'TR'
}

# создание базового набора стран и некоторых городов в них

cities = {
    'UZ': 'Газли',
    'TR': 'Сарыгерме',
    'DE': 'Мюнхен'
}

# добавление нескольких городов

sities['ZW'] = 'Гверу'
sities['RU'] = 'Москва'

# вывод нескольких городов

print('-' * 10)
print('В стане ZW есть город: ', cities['ZW'])
print('В стране RU есть город: ', cities['RU'])

# вывод некоторых стран
print('-' * 10)
print('В Турции есть город : ', sities[states['Турция']])
print('В Германии есть город: ', sities[states['Германия']])

# вывод аббревеатур всех стран
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} имеет аббревеатуру {abbrev}')

# вывод всех городов в странах
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'В стране {abbrev} есть город {city}')

# а теперь сразу оба типа данных
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'В стране {state} используется аббревеатура {abbrev}')
    print(f'и есть город {cities[abbrev]}')
