import os
from lists.destinations import destino_fallback
import shutil
from lists.groups import txtgroup, imggroup, excelgroup, zipgroup, pdfgroup, videogroup
from lists.destinations import documenttxt, documentimg, documentexcel, documentzip, documentpdf, documentvideo

def mover_para_documents(caminho_completo):
    try:
        file = os.path.basename(caminho_completo)
        ext = os.path.splitext(file)[1]
        if ext in txtgroup:
            shutil.move(caminho_completo, documenttxt)
            print(f"Arquivo {file} movido para {documenttxt}")
        elif ext in imggroup:
            shutil.move(caminho_completo, documentimg)
            print(f"Arquivo {file} movido para {documentimg}")
        elif ext in excelgroup:
            shutil.move(caminho_completo, documentexcel)
            print(f"Arquivo {file} movido para {documentexcel}")
        elif ext in zipgroup:
            shutil.move(caminho_completo, documentzip)
            print(f"Arquivo {file} movido para {documentzip}")
        elif ext in pdfgroup:
            shutil.move(caminho_completo, documentpdf)
            print(f"Arquivo {file} movido para {documentpdf}")
        elif ext in videogroup:
            shutil.move(caminho_completo, documentvideo)
            print(f"Arquivo {file} movido para {documentvideo}")
        else:
            shutil.move(caminho_completo, destino_fallback)
            print(f"Arquivo {file} movido para {destino_fallback}")
    except Exception as e:
        print(f"Erro ao mover o arquivo {os.path.basename(caminho_completo)}: {e}")