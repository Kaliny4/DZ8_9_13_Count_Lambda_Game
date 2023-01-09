"""
Сделать программу в виде функций в которой нужно будет угадывать число.
"""
import random


def guess_num():
    right_num = random.randint(0, 100)
    n = -1

    while n != right_num:
        n = input('Ввести с клавиатуры целое число от 0 до 100: ')
        if not n.isdigit():
            continue
        else:
            n = int(n)
            if n != right_num:
                print('Try again')
                continue
            else:
                print('Right!')
                break


guess_num()



