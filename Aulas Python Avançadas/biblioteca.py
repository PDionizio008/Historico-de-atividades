import os
lista_arquivos = os.listdir("arquivos")

print(lista_arquivos)

print(lista_arquivos[5])

# os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt")

for arquivo in lista_arquivos:
    if '.txt' in arquivo:
        if '22' in arquivo:
             os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
        else:
           os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")
