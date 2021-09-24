print('Давайте попрактикуемся!')
print('Вы должны знать об уравляющих последовательностях с символом \\, которые:')
print('\n управляют переносом строк и \t отступами')

poem = '''
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\t\tи никогда не отпускать!
'''

print('-----------------------')
print(poem)
print('-----------------------')

five = 10 - 2 + 3 - 6
print(f'Здесь должна быть пятерка: {five}')

def secret_formula(started):
    jelly_beance = started * 500
    jars = jelly_beance / 1000
    craters = jars / 100
    return jelly_beance, jars, craters

start_point = 10000
beance, jars, craters = secret_formula(start_point)

#Помните, что это еще один способ форматирования строки
print('Начиная с: {}'.format(start_point))
#Так же, как со строкой f''
print(f'У нас есть {beance} бобов, {jars} банок и {craters} ящиков.')

start_point = start_point / 10

print('Мы также можем сделать это таким обрзом:')
formula = secret_formula(start_point)
#Простой способ применить список к форматируемой строке
print('У нас есть {} бобов, {} банок и {} ящиков.'.format(*formula))
