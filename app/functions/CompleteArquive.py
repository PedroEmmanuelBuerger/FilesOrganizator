import time
def arquivo_completo(path):
    while True:
        try:
            with open(path, 'r+'):
                break
        except IOError:
            time.sleep(1)
    return True