import os

# Lista todos os arquivos na pasta "documentos"
lista_documentos = os.listdir("documentos")

# Mostra a lista completa
print(lista_documentos)

# Exibe o 6º item da lista (índice 5)
if len(lista_documentos) > 5:
    print(lista_documentos[5])

# Percorre cada arquivo na lista
for arquivo in lista_documentos:
    if 'documentos' in arquivo:  # Corrigido: verificar se "documentos" está no nome do arquivo
        print(arquivo)
        if arquivo.endswith('.docx'):
            os.rename(f"documentos/{arquivo}", f"documentos/word_{arquivo}")
        elif arquivo.endswith('.xlsx'):
            os.rename(f"documentos/{arquivo}", f"documentos/excel_{arquivo}")
        elif arquivo.endswith('.pptx'):
            os.rename(f"documentos/{arquivo}", f"documentos/powerpoint_{arquivo}")
