way = 'C:\\Users\\Kaznin\\Documents\\Morrowind\\myfile.txt'

replace_symbols_in_way = way.replace('\\', ' ')
split_in_way = replace_symbols_in_way.split(' ')

file = split_in_way[-1].replace('.', ' ')
split_file = file.split()
name_file = split_file[0]

print(f'Имя файла "{name_file}"')