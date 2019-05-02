import time

now = time.ctime()

def write(files):
    with open('espelho_log.txt', 'a') as escreve:
        escreve.write('{}: Existem mais de 3 arquivos: {}\n'.format(now, files))		
