def user_text():
    ut = input('') # Мама мыла собаку? Нет! Нет-нет! Мама мыла раму!
    nut = ut.replace('.', '') # весь replace для чистки текста от символов
    nut1 = nut.replace(',', '')
    nut2 = nut1.replace('-', ' ')
    nut3 = nut2.replace('!', '')
    nut4 = nut3.replace('?', '')
    nut5 = nut4.lower() # весь текст приводим к строчному виду
    nut6 = nut5.split() # бахнули список

    d= {} # создали словарь

    for i in nut6:
        d[i] = nut6.count(i)
    return d

print(user_text())