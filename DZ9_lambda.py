"""
Написать лямбда-функцию определяющую чётное/нечётное.
Функция принимает параметр (число) и если чётное, то выдаёт слово “чётное”,
если нет - то “не чётное”.
"""

chet_nechet = lambda n: print('чётное') if n % 2 == 0 else print('не чётное')
chet_nechet(int(input('Enter the number: ')))
