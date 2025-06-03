# import os 
# os.system("cls")

# # Cadastro inicial
# lista_produto = ['ipad', 'iphone', 'airpod', 'macbook']
# preco = ['3000', '5000', '800', '10000']

# print(lista_produto[0])

# # Criação do dicionário de produtos
# dic_produto = {'ipad': 3000, 'iphone': 5000, 'airpod': 800, 'macbook': 10000}
# print(dic_produto)

# # Encontrar valor no dicionário
# print(dic_produto['ipad'])

# # Adicionar novo produto ao dicionário
# dic_produto['apple watch'] = 8000
# print(dic_produto)

# # Editar valor no dicionário
# dic_produto['airpod'] = 2000
# print(dic_produto)

# # Atualizar valor do produto com cálculo
# dic_produto['iphone'] = dic_produto['iphone'] * 1.3
# print(dic_produto)

# # Remover valor do dicionário
# dic_produto.pop('apple watch')
# print(dic_produto)

# # Adicionar novamente o produto
# dic_produto['apple watch'] = 8000
# print(dic_produto)

# # Verificador de produto
# if 'iphone' in dic_produto:
#     print('O produto existe')
# else:
#     print('O produto não existe')

# # Verificador pelo valor
# if 3000 in dic_produto.values():
#     print('O produto com esse valor existe')
# else:
#     print('Não existe produto com esse valor')

# # Cadastro de novos produtos via teclado
# print("\n--- Cadastro de novos produtos ---")
# for i in range(2):  # você pode ajustar a quantidade aqui
#     nome = input("Digite o nome do produto: ")
#     valor = float(input("Digite o preço do produto: "))
#     dic_produto[nome] = valor

# print("\nDicionário após cadastro:")
# print(dic_produto)

# # Aumento de 50% nos valores dos produtos
# for produto in dic_produto:
#     dic_produto[produto] = dic_produto[produto] * 1.5

# print("\nDicionário após aumento de 50% nos preços:")
# print(dic_produto)





# Cadastro de produto e preco no dicionario

# Atualize os valores dos produtos no dicionario com um aumento de 50%





# Criar um dicionário com produtos
meus_produtos = {"Mouse": 150, "Teclado": 200, "Monitor": 800, "Gabinete": 500}

# Converter o dicionário para usar chaves em letras minúsculas internamente
meus_produtos = {produto.lower(): preco for produto, preco in meus_produtos.items()}

# Mostrar todos os produtos e seus preços
print("\n--- Lista de produtos ---")
for produto, preco in meus_produtos.items():
    print(f"{produto.capitalize()}: R$ {preco:.2f}")

# Mostrar o preço de um produto informado pelo usuário
produto_busca = input("\nDigite o nome de um produto para ver o preço: ").lower()
if produto_busca in meus_produtos:
    print(f"O preço do {produto_busca.capitalize()} é R$ {meus_produtos[produto_busca]:.2f}")
else:
    print("Produto não encontrado.")

# Atualizar o preço de um produto
produto_atualizar = input("\nDigite o nome do produto que deseja atualizar o preço: ").lower()
if produto_atualizar in meus_produtos:
    try:
        novo_preco = float(input("Digite o novo preço: "))
        meus_produtos[produto_atualizar] = novo_preco
        print("Preço atualizado com sucesso.")
    except ValueError:
        print("Preço inválido. A atualização foi cancelada.")
else:
    print("Produto não encontrado.")

# Adicionar um novo produto
produto_novo = input("\nDigite o nome de um novo produto para adicionar: ").lower()
try:
    preco_novo = float(input("Digite o preço do novo produto: "))
    meus_produtos[produto_novo] = preco_novo
    print("Produto adicionado com sucesso.")
except ValueError:
    print("Preço inválido. O produto não foi adicionado.")

# Remover um produto
produto_remover = input("\nDigite o nome de um produto para remover: ").lower()
if produto_remover in meus_produtos:
    meus_produtos.pop(produto_remover)
    print("Produto removido com sucesso.")
else:
    print("Produto não encontrado.")

# Mostrar o dicionário final com 10% de desconto nos preços
print("\n--- Dicionário final de produtos (com 10% de desconto) ---")
for produto, preco in meus_produtos.items():
    preco_com_desconto = preco * 0.9
    print(f"{produto.capitalize()}: R$ {preco_com_desconto:.2f}")

