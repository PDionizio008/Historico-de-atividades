frutas= ["Uva", "Manga", "Laranja", "Abacate","Mexirica"]
numeros = [1,2,3,4,5]
variados = [1, "dois", 3, "quatro", True]
print(frutas)
# Imprimir por posição o valor da lista
print(frutas[-1])

print(numeros)
print(numeros[-1])

print(variados[2])

# Subistituir valor na lista

frutas[1] = "Abacaxi"
print(frutas)

variados [1] = 2
print(variados)
# Adicionar valor na lista
numeros.append(6)
print(numeros)

frutas.insert(0,"Cupu")
print(frutas)

frutas.insert(1,"Tomate")
print(frutas)

frutas.remove("Tomate")
print(frutas)

frutas.pop()
print(frutas)

# Quantas vezes o valor aparece na lista

print(numeros.count(1))
 #Contas quantas elemetos tem na lista
print(len(numeros))

# Ordem alfabetica

frutas.sort()
print(frutas)

# Ordem inversa

numeros.reverse()
print(numeros)

# Cria Lista com Nomes
# Adicionar mais 3 nomes
# Excluir 2 nomes
# Vão colocar em ordem alfabetica

nomes = ["Amanda", "Raimunda", "Italo"]


