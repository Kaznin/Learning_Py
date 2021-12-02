def is_palindrom(number):

    number_to_str = str(number) # преобразование в строку
    number_to_list = list(number_to_str) # проебразование в список
    exception_list = number_to_list.copy() # копия исходного списка
#    print(exception_list) # для проверки значений
    number_to_list.reverse() # развернули список
#    print(number_to_list) # для проверки значений

    if exception_list == number_to_list:
        return print(f'Палиндром, т.к. исходное значение {exception_list}, обратное  {number_to_list}')
    else:
        return print(f'Не палиндром, т.к. исходное значение {exception_list}, обратное  {number_to_list}')

is_palindrom(9)