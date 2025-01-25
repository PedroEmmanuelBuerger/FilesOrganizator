from functions.MoveToDocuments import mover_para_documents
import os
import time
from lists.destinations import destinotxt, destinoimg, destinoexcel, destinozip, destinopdf

def verificar_documents():
    destinos = [destinotxt, destinoimg, destinoexcel, destinozip, destinopdf]
    for destino in destinos:
        arquivos_atuais = set(os.listdir(destino))
        for file in arquivos_atuais:
            caminho_completo = os.path.join(destino, file)
            if os.path.isfile(caminho_completo):
                tempo_criacao = os.path.getctime(caminho_completo)
                tempo_atual = time.time()
                if tempo_atual - tempo_criacao >= 604800:
                    mover_para_documents(caminho_completo)