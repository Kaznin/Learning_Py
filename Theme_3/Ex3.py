list_i = []

for i in range(1, 1000):
    a = int(i ** 0.5)
    if a >= 2:
        is_simple = True
        for j in range(2, a+1):
            if i % j == 0:
                is_simple = False
        if is_simple:
            list_i.append(i)
    else:
        list_i.append(i)


print(list_i)