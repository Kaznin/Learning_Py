lucky_list = []

# зададим верхнюю и нижнюю границы
start = '000000'
finish = '999999'

for i in range(int(start), int(finish)):
    i = i + 1
    j = str(i).zfill(6) # в i число, например, 1. в j преобразуем в строку вида 000001
    left_j = int(j[0]) + int(j[1]) + int(j[2]) # находим сумму первых 3 значений
    right_j = int(j[3]) + int(j[4]) + int(j[5]) # находим сумму вторых 3 значений

    if left_j == right_j:
        lucky_list.append(j)

print(lucky_list)