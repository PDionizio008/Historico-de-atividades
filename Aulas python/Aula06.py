
# num = int(input("Digite um numero para ver a tabuada: "))

# for i in range(11):
#  resultado = num * i
#  print(f"{num} * {i} = {resultado}")
# print("Fim da Tabuada")

# num = 5

# if num % 2 == 0:
#     print("Numero Par")
# else:
#     print("Impar")

# for num in range(0, 101):
#     if num % 2 == 0:
#         print(num)

# lista = [1000, 800, 2000, 2500, 700, 650, 999]
# meta = 1000

# for i, valor in enumerate(lista):
#     if valor >= meta:
#         print(f"Funcionário {i + 1} vendeu R${valor} e ele receberá a devida comissão!")
#     else:
#         print(f"Funcionário {i + 1} vendeu R${valor} e **não** atingiu a meta.")

# Maior ou Igual a 7 aprovado

# Maior ou igual a 5 e menor 7 recuperação

# menor que 5 reprovado

# notas = [8.5, 6.0, 4.5, 7.0, 5.5, 3.0, 9.0]

# for i, nota in enumerate(notas):
#     if nota >= 7:
#         print(f"Aluno {i + 1}: nota {nota} → Aprovado")
#     elif nota >= 5:
#         print(f"Aluno {i + 1}: nota {nota} → Recuperação")
#     else:
#         print(f"Aluno {i + 1}: nota {nota} → Reprovado")

# # Lista para armazenar os números
# numeros = []

# # Recebe 5 números do usuário
# for i in range(5):
#     numero = float(input(f"Digite o {i + 1}º número: "))  # Recebe um número e converte para float
#     numeros.append(numero)  # Adiciona o número na lista

# # Soma de todos os números
# soma = sum(numeros)

# # Exibe o resultado
# print(f"A soma dos números é: {soma}")
# Dados de login
user = 'Admin'
password = '12345'

# Tentativas de login
for i in range(3):
    # Solicitar nome de usuário e senha
    usuario = input("Usuário: ")
    usuario_senha = input("Senha: ")

    # Verificar se as credenciais estão corretas
    if usuario == user and usuario_senha == password:
        print("Login bem-sucedido! Bem-vindo ao sistema.")
        break  # Sai do loop após o login bem-sucedido
    else:
        if i < 2:  # Se não for a última tentativa
            print(f"Senha incorreta! Você tem {2 - i} tentativa(s) restante(s).")
        else:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")




