# # # Crie uma lista com 5 itens de mercado
# # # Remova 2 itens
# # # Adicione 3 novos itens
# # # Mostre a lista final em ordem alfabética

# # produtos = ["Extrato de tomate","Macarrão parafuso","Cebola","Tomate","Cheiro Verde"]
# # print(produtos)

# # produtos.remove ("Cebola")
# # produtos.remove ("Cheiro Verde")
# # print(produtos)

# # produtos.extend(["Molho Branco", "Presunto", "Mussarela"])
# # print(produtos)

# # produtos.sort()
# # print(produtos)

# lista_carros = [ ]
# carro1 = input("Digite carro 1 : ")
# carro2 = input("Digite carro 2 : ")
# carro3  = input("Digite carro 3 : ")

# # lista_carros.append(carro1)
# # lista_carros.append(carro2)
# # lista_carros.append(carro3)
# # Adicionar mais de um elemento de uma vez
# carro2 = carro2.lower()
# lista_carros.extend([carro1,carro2,carro3])
# print(lista_carros)

# # Procurar valor dentro de uma lista
# print("marea" in lista_carros)

# lista_times = [ ]

# time1 = input("Digite Time 1 :")
# time2 = input("Digite Time 2 :")
# time3 = input("Digite Time 3 :")

# time1 = time1.capitalize()
# time2 = time2.capitalize()
# time3 = time3.capitalize()

# lista_times.extend([time1,time2,time3])

# buscar_time = input("Digite o nome do time : ")

# print(lista_times)
# print(buscar_time in lista_times)

# Crie uma lista vazia
# Com input adicione á marca de celulares
# Crie uma variavel para buscar a marca do celular
# Coloque um metodo que transforme o texto da busca do  celular de forma que encontre o produto, não importando como o texto está.

# Print a lista com todas as marcas
# print se o produto esta na lista ou não.

# buscar_marca = [ ]

# for i in range(4):
#     marca = input(f"Digite a marca {i+1} do celular: ").strip().capitalize()
#     buscar_marca.append(marca)

# busca = input("Digite a marca que você quer buscar: ").strip().capitalize()
# print("Lista de marcas cadastradas:", buscar_marca)

# if busca in buscar_marca:
#     print(" O produto está na lista!")
# else:
#     print(" O produto NÃO está na lista.")

lista_marca = [ ]

marca1 = input("Digite a primeira marca: ")
marca2 = input("Digite a segunda marca: ")
marca3 = input("Digite a terceira marca: ")
marca4 = input("Digite a quarta marca: ")

lista_marca.extend([marca1, marca2, marca3, marca4])

buscar_marca = input("Buscar marca: ").casefold()

lista_nova = ([marca.casefold() for marca in lista_marca])

print(lista_nova)
print(buscar_marca in lista_nova)
