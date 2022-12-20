def countries_input():
    b = []
    for i in range(2):
        a = input(f'{i}-ая страна: ').split(' ')
        b.append(dict.fromkeys(a, a[0]))
    return b


print(countries_input())