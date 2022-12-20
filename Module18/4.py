new_string = input('Введите строку: ').split(' ')
new_title_list = [x.title() for x in new_string]
print(' '.join(new_title_list))
