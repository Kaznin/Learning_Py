import datetime
import calendar

'''
Программа вычисляет новую дату. На входе получаем 2 агрумента: дата пользователя и число, являющееся количеством
месяцев, которое нужно добавить или отнять от латы пользователя.
'''

def change_data(user_date, user_number):


    count_user_month = 0
    user_date = datetime.datetime.strptime(user_date, '%d.%m.%y')
    user_year = user_date.year
    user_month = user_date.month

    while count_user_month != abs(user_number):
        if user_number > 0:
            user_month += 1
            if user_month == 13:
                user_month = 1
                user_year += 1
            get_sum_days_in_month = calendar.monthrange(user_year, user_month) # calendar.monthrange(year, month)) возвращает двойной кортеж c первым рабочем днем месяца и количество дней в месяце для указанного года year и месяца month
            count_user_month += 1 # тут работает счетчик. После совпадаение значения со значением переменной user_month программа остановится
            user_date = user_date + datetime.timedelta(days=get_sum_days_in_month[1])


        elif user_number < 0:
            user_month -= 1
            if user_month == 0:
                user_month = 12
                user_year -= 1
            get_sum_days_in_month = calendar.monthrange(user_year, user_month)
            count_user_month += 1
            user_date = user_date - datetime.timedelta(days=get_sum_days_in_month[1])


    return user_date

print(change_data('02.06.89', -10))