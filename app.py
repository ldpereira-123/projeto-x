#!/usr/local/bin/python

import os
import time
from write_on_file import write

path = 'C:/Users/sys_ldpereira/Documents/teste'
count = 0
files = []
now = time.ctime()

# r = root, d = directories , f = files
while True:
    for r, d, f in os.walk(path):
        d.clear()
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(file))
                count += 1

            elif '.125' in file:
                files.append(os.path.join(file))
                count += 1

    if count >= 3:
        print('{}: Existe mais de 3 arquivos dentro do diretório!'.format(now))
        #print(files)
        write(files)
        files = []
        count = 0
        time.sleep(5)

    else:
        print('{}: Quantidade de arquivos dentro da pasta: {}'.format(now, count))
        time.sleep(5)
        count = 0

