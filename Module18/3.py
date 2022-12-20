file_name = input('Название файла: ')
taboo_symbols = tuple('@№$%^&*()')
if file_name.startswith(taboo_symbols):
    print('Ошибка: название начинается на один из специальных символов.')
elif not (file_name.endswith('.txt') or file_name.endswith('.doc')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')