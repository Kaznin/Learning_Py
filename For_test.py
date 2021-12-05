import calendar
import datetime

print(calendar.monthrange(1989, 2)) #возвращает двойной кортеж c первым рабочем днем месяца и количество дней в месяце для указанного года year и месяца month.
print(len(calendar.month(1989, 2)))

user_date = '02.02.89'
user_date = datetime.datetime.strptime(user_date, '%d.%m.%y')
print(user_date.month)