import os
import shutil
from tkinter.filedialog import askdirectory
from datetime import datetime
import time

# Loop para rodar a cada 5 minutos
while True:
    # 1. Seleciona a pasta de origem
    pasta_selecionada = askdirectory(title="Selecione a pasta para backup")
    if not pasta_selecionada:
        print("Nenhuma pasta selecionada. Encerrando...")
        break

    print(f"Pasta selecionada: {pasta_selecionada}")

    # 2. Lista todos os arquivos e pastas na origem
    try:
        lista_arquivos = os.listdir(pasta_selecionada)
    except PermissionError:
        print("Permissão negada para acessar a pasta.")
        continue

    print(f"Arquivos encontrados: {lista_arquivos}")

    # 3. Cria nome da pasta de backup com data e hora
    agora = datetime.now()
    nome_pasta_backup = 'backup_' + agora.strftime('%Y-%m-%d_%H-%M-%S')
    nome_completo_backup = os.path.join(pasta_selecionada, nome_pasta_backup)

    # 4. Cria a pasta de backup
    try:
        os.makedirs(nome_completo_backup)
        print(f"Pasta '{nome_pasta_backup}' criada.")
    except FileExistsError:
        print(f"Pasta '{nome_pasta_backup}' já existe.")
        pass

    # 5. Copia arquivos e pastas, ignorando pastas de backup
    for arquivo in lista_arquivos:
        caminho_original = os.path.join(pasta_selecionada, arquivo)
        caminho_destino = os.path.join(nome_completo_backup, arquivo)

        # Evita copiar a própria pasta de backup
        if arquivo == nome_pasta_backup or arquivo.startswith("backup_"):
            print(f"Ignorando pasta de backup: {arquivo}")
            continue

        try:
            if os.path.isfile(caminho_original):
                print(f"Copiando arquivo: {arquivo}")
                shutil.copy2(caminho_original, caminho_destino)

            elif os.path.isdir(caminho_original):
                print(f"Copiando pasta: {arquivo}")
                if os.path.exists(caminho_destino):
                    shutil.rmtree(caminho_destino)
                shutil.copytree(caminho_original, caminho_destino)
        except Exception as e:
            print(f"Erro ao copiar {arquivo}: {e}")

    print("Backup finalizado. Aguardando 5 minutos...\n")
    time.sleep(300)  # Espera 5 minutos (300 segundos)

