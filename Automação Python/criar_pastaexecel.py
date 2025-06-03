# import os
# from openpyxl import Workbook

# # Caminho para a área de trabalho (Windows)
# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# # Nome da pasta e caminho completo
# folder_name = "Clientes"
# folder_path = os.path.join(desktop_path, folder_name)

# # Cria a pasta se não existir
# os.makedirs(folder_path, exist_ok=True)

# # Nome do arquivo Excel e caminho completo
# file_name = "dados_clientes.xlsx"
# file_path = os.path.join(folder_path, file_name)

# # Dados dos clientes
# clientes = [
#     ["Ana Clara Martins", "ana.martins@gmail.com", "11981112233", "15/02/1989"],
#     ["Carlos Henrique Lima", "carlos.lima@hotmail.com", "11982223344", "03/11/1985"],
#     ["Juliana Souza Reis", "juliana.reis@yahoo.com", "11983334455", "27/06/1992"],
#     ["Felipe Andrade Rocha", "felipe.rocha@outlook.com", "11984445566", "08/09/1987"],
#     ["Larissa Gomes Vieira", "larissa.vieira@gmail.com", "11985556677", "19/01/1995"],
#     ["Bruno ferreira Costa", "bruno.costa@live.com", "11986667788", "22/04/1990"],
#     ["Patricia Mello Cardoso", "patricia.cardoso@uol.com.br", "11987778899", "30/10/1983"],
#     ["Ricardo Alves Pinto", "ricardo.pinto@gmail.com", "11988889900", "14/12/1988"],
#     ["Marina Duarte Lopes", "marina.lopes@icloud.com", "11989990011", "11/07/1994"],
#     ["Diego Ribeiro Teixeira", "diego.teixeira@protonmail.com", "11990001122", "05/05/1991"]
# ]

# # Cria o arquivo Excel
# wb = Workbook()
# ws = wb.active
# ws.title = "Clientes"

# # Cabeçalhos
# ws.append(["Nome", "Email", "Telefone", "Data de Nascimento"])

# # Adiciona os dados
# for cliente in clientes:
#     ws.append(cliente)

# # Salva o arquivo
# wb.save(file_path)

# print(f"Arquivo criado com sucesso em: {file_path}")


import os
import pandas as pd

# Definindo o caminho da pasta
folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "Clientes")

# Cria a pasta se não existir
os.makedirs(folder_path, exist_ok=True)

# Definindo o caminho completo do arquivo
file_path = os.path.join(folder_path, "dados_clientes.xlsx")

# Criando o DataFrame com os cabeçalhos e sem dados
df = pd.DataFrame(columns=["Nome", "Email", "Telefone", "Data de Nascimento"])

# Salvando o DataFrame no Excel
df.to_excel(file_path, index=False)

print(f"Arquivo criado com sucesso em: {file_path}")


