import os
import shutil

filelocations = r"C:\Users\pedro.silva\Downloads"

destinotxt = r"C:\Users\pedro.silva\Downloads\txt"
destinopng = r"C:\Users\pedro.silva\Downloads\png"

listdestino = [destinotxt, destinopng]

for root, dirs, files in os.walk(filelocations):
    if root in listdestino:
        continue
    
    for file in files:
        path_complete = os.path.join(root, file)
        
        name, ext = os.path.splitext(file)
        
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
        else:
            print(f"Arquivo {file} não é .txt")

#try:
#    shutil.move(arquivo_origem, destino)
#    print(f"Arquivo movido para {destino}")
#except FileNotFoundError:
#    print("Arquivo ou diretório de origem não encontrado.")
#except PermissionError:
#    print("Permissão negada para mover o arquivo.")
#except Exception as e:
#    print(f"Erro ao mover o arquivo: {e}")