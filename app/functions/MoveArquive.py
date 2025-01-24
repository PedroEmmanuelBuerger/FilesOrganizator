import shutil
from lists.destinations import destinotxt, destinoimg, destinoexcel, destinozip, destinopdf
from lists.groups import txtgroup, imggroup, excelgroup, zipgroup, pdfgroup

def mover_arquivo(file, ext, path_complete):
    if ext in txtgroup:
        try:
            shutil.move(path_complete, destinotxt)
            print(f"Arquivo {file} movido para {destinotxt}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file}: {e}")
    elif ext in imggroup:
        try:
            shutil.move(path_complete, destinoimg)
            print(f"Arquivo {file} movido para {destinoimg}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file}: {e}")
    elif ext in excelgroup:
        try:
            shutil.move(path_complete, destinoexcel)
            print(f"Arquivo {file} movido para {destinoexcel}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file}: {e}")
    elif ext in zipgroup:
        try:
            shutil.move(path_complete, destinozip)
            print(f"Arquivo {file} movido para {destinozip}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file}: {e}")
    elif ext in pdfgroup:
        try:
            shutil.move(path_complete, destinopdf)
            print(f"Arquivo {file} movido para {destinopdf}")
        except Exception as e:
            print(f"Erro ao mover o arquivo {file}: {e}")