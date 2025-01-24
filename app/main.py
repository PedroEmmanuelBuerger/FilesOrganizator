import os
from functions.MoveArquive import mover_arquivo
from functions.CompleteArquive import arquivo_completo
from lists.destinations import listdestino
from lists.groups import allgroups
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

filelocations = r"C:\Users\pedro.silva\Downloads"

for destino in listdestino:
    if not os.path.exists(destino):
        os.makedirs(destino)

def verificar_pasta():
    arquivos_atuais = set(os.listdir(filelocations))
    for file in arquivos_atuais:
        caminho_completo = os.path.join(filelocations, file)
        ext = os.path.splitext(file)[1]
        if os.path.isfile(caminho_completo) and ext in allgroups:
            if arquivo_completo(caminho_completo):
                mover_arquivo(file, ext, caminho_completo)

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file = os.path.basename(event.src_path)
            ext = os.path.splitext(file)[1]
            if file.startswith("~$") or file.endswith(".tmp"):
                return
            if ext in allgroups:
                if arquivo_completo(event.src_path):
                    mover_arquivo(file, ext, event.src_path)

observer = Observer()
event_handler = FileHandler()
observer.schedule(event_handler, filelocations, recursive=False)

observer.start()

try:
    print("Monitorando pasta de Downloads... Pressione Ctrl+C para parar.")
    while True:
        verificar_pasta()
except KeyboardInterrupt:
    observer.stop()
observer.join()
