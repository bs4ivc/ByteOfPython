#!/usr/bin/python3

import os
import time

# 1.Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['/media/bs4ivc/Films/www/Projects/Python/ByteOfPython', '"/media/bs4ivc/Films/www/Projects/Python/New Project"']
# Заметьте, что для имен, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2.Резервные копии должны храниться в основном каталоге резерва.
target_dir = '/home/bs4ivc/Documents' # Подставте тот путь, которій ві будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив.
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии.
if os.system(zip_command) == 0:
    print('Резервная копияуспешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

