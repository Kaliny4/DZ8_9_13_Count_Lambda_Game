"""
Дан список чисел.
Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
Подсказка: для хранения данных использовать словарь (ключ - само число, а значение -
сколько раз оно встречается).
Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.

"""
list_of_numbers = [3, 5, 6, 7, 10, 30, 25, 6, 7, 30, 30, 3, 3, 3, 3]


def each_num(z):
    result = {}
    for num in z:
        if result.get(num, None):
            result[num] += 1
        else:
            result[num] = 1
    return result


print(each_num(list_of_numbers))


#ще варіант

def each_num1(b):
    res = {}.fromkeys(b, 0)
    for i in b:
        res[i] += 1
    print(res)


each_num1(list_of_numbers)

