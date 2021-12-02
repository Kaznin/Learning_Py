import datetime
count = 0

def change_data(user_date, user_number):

    months_dict = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31,
              '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

    months_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    actuality_month = []
    work_month = []

    for i in months_list:
        if months_list[i] == user_date[3:5]:
            actuality_month.append(months_list[i])

    for n in user_number:
        count = months_list[actuality_month]

    user_date = datetime.datetime.strptime(user_date, '%d.%m.%y')
    new_date = user_date + datetime.timedelta(days=user_number*30.5)

    return new_date

print(change_data('02.02.89', 1))