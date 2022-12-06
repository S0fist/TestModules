import ipaddress

try:
    ipaddress.IPv4Address(input('Введите IP: '))
    print('IP корректен')
except Exception:
    print('Не верный ввод IP')
