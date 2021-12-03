import time
import random

'''
Пишем генератор числа произвольной длинны, который поместим в декоратор. Декоратор считает время работы программы.
We're writing generator fo own number which work in a decorator. A decorator count time work.
'''

def time_counter_decor(fn):
    def wrapper():
        start_time = time.time()
        a = fn()
        finish_time = time.time()
        print(f'Функция работала {finish_time - start_time} секунд')
        return a
    return wrapper

@time_counter_decor
def number_generator():
    user_count = int(input('Сколько символов должно быть в числе? '))
    count_list = []

    while len(count_list) < user_count:
        count_list.append(random.randint(0, 9))

    finish_count = str(''.join(map(str, count_list)))
    return print(finish_count)


number_generator()
