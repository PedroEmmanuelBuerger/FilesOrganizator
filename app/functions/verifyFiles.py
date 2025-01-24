from functions.MoveArquive import mover_arquivo
from functions.CompleteArquive import arquivo_completo
import os
from lists.groups import allgroups
from lists.destinations import filelocations

def verificar_pasta():
    arquivos_atuais = set(os.listdir(filelocations))
    for file in arquivos_atuais:
        caminho_completo = os.path.join(filelocations, file)
        ext = os.path.splitext(file)[1]
        if os.path.isfile(caminho_completo) and ext in allgroups:
            if arquivo_completo(caminho_completo):
                mover_arquivo(file, ext, caminho_completo)