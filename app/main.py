import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

filelocations = r"C:\Users\pedro.silva\Downloads"
destinotxt = r"C:\Users\pedro.silva\Downloads\txt"
destinopng = r"C:\Users\pedro.silva\Downloads\png"
listdestino = [destinotxt, destinopng]

for destino in listdestino:
    if not os.path.exists(destino):
        os.makedirs(destino)

def mover_arquivo(file, ext, path_complete):
    if ext == ".txt":
        try:
            shutil.move(path_complete, destinotxt)
            print(f"Arquivo {file} movido para {destinotxt}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file}: {e}")
    elif ext == ".png":
        try:
            shutil.move(path_complete, destinopng)
            print(f"Arquivo {file} movido para {destinopng}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file}: {e}")

def arquivo_completo(path):
    while True:
        try:
            with open(path, 'r+'):
                break
        except IOError:
            time.sleep(1)
    return True

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file = os.path.basename(event.src_path)
            ext = os.path.splitext(file)[1]
            if ext in [".txt", ".png"]:
                if arquivo_completo(event.src_path):
                    mover_arquivo(file, ext, event.src_path)

observer = Observer()
event_handler = FileHandler()
observer.schedule(event_handler, filelocations, recursive=False)

observer.start()

try:
    print("Monitorando pasta de Downloads... Pressione Ctrl+C para parar.")
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
