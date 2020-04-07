#!/usr/bin/python3

# 'ab' - сокращение от 'a'ddress 'b'ook

ab = { 'Swaroop'    : 'swaroop@swaroopch.com',
       'Larry'      : 'larry@wall.org',
       'Matsumoto'  : 'matz@ruby-lanf.org',
       'Spammer'    : 'spammer@hotmail.com'
    }

print("Адрес Swaroop'a:", ab['Swaroop'])

# Удаление пары ключ-знфчение

del ab['Spammer']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name,address))

# Добавление пары ключ-значение

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

