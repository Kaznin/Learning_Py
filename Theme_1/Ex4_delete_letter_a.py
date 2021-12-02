phrase = 'Калашников'

length_phrase = len(phrase) #10

new_phrase = phrase.replace('а', '')
new_length_phrase = len(new_phrase) # Клшников
delete_letter_a = length_phrase - new_length_phrase # 2

print(f'Новое слово "{new_phrase}", удалено {delete_letter_a} буквы "а".')
