import os
import pandas as pd

# Lista de clientes
clientes = [
    {"nome": "Ana Clara Martins", "email": "ana.martins@gmail.com", "telefone": "11981112233", "data_nascimento": "15/02/1989"},
    {"nome": "Carlos Henrique Lima", "email": "carlos.lima@hotmail.com", "telefone": "11982223344", "data_nascimento": "03/11/1985"},
    {"nome": "Juliana Souza Reis", "email": "juliana.reis@yahoo.com", "telefone": "11983334455", "data_nascimento": "27/06/1992"},
    {"nome": "Felipe Andrade Rocha", "email": "felipe.rocha@outlook.com", "telefone": "11984445566", "data_nascimento": "08/09/1987"},
    {"nome": "Larissa Gomes Vieira", "email": "larissa.vieira@gmail.com", "telefone": "11985556677", "data_nascimento": "19/01/1995"},
    {"nome": "Bruno ferreira Costa", "email": "bruno.costa@live.com", "telefone": "11986667788", "data_nascimento": "22/04/1990"},
    {"nome": "Patricia Mello Cardoso", "email": "patricia.cardoso@uol.com.br", "telefone": "11987778899", "data_nascimento": "30/10/1983"},
    {"nome": "Ricardo Alves Pinto", "email": "ricardo.pinto@gmail.com", "telefone": "11988889900", "data_nascimento": "14/12/1988"},
    {"nome": "Marina Duarte Lopes", "email": "marina.lopes@icloud.com", "telefone": "11989990011", "data_nascimento": "11/07/1994"},
    {"nome": "Diego Ribeiro Teixeira", "email": "diego.teixeira@protonmail.com", "telefone": "11990001122", "data_nascimento": "05/05/1991"}
]

# Definir o caminho da pasta
folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "Clientes")
os.makedirs(folder_path, exist_ok=True)  # Cria a pasta se não existir

# Definir o caminho completo do arquivo
file_path = os.path.join(folder_path, "dados_clientes.xlsx")

# Converter a lista de dicionários para DataFrame do pandas
df = pd.DataFrame(clientes)

# Renomear as colunas para ficarem mais organizadas no Excel
df.rename(columns={
    "nome": "Nome",
    "email": "Email",
    "telefone": "Telefone",
    "data_nascimento": "Data de Nascimento"
}, inplace=True)

# Salvar no Excel
df.to_excel(file_path, index=False)

print(f"Arquivo Excel criado com sucesso em: {file_path}")
 