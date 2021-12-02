a = 'Мама мыла раму, а папа не мыл раму.'

delete_symbol_in_a = a.replace(',', '')
delete_symbol_in_a_2 = delete_symbol_in_a.replace('.', '')

length_string = delete_symbol_in_a_2.split()

print(len(length_string)) # 8