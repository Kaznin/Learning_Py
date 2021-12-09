import datetime

def change_month(user_date, user_months=0):
    a = datetime.datetime.strptime(user_date, '%d.%m.%y')
    b = a.month + user_months

    c = b > 12

    if b > 12:
        b = b - 12

    if c:
        d = a.year + 1
    else:
        d = a.year

    new_user_date = datetime.datetime(d, b, a.day)

    return new_user_date.strftime('%d.%m.%Y')

print(change_month('31.03.01', 24))