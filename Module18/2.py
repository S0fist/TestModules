length_string = input('Введите строку: ').split(' ')
length_list = [len(x) for x in length_string]
print('Самое длинное слово: {}'.format(length_string[length_list.index(max(length_list))]))
print('Длина этого слова: {}'.format(max(length_list)))
