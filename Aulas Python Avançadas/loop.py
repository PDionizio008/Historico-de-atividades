# Loop para (listas, string e etc)
for i in range(10):
    print(i)

# Loop While (executa enquanto condição for verdadeira)
contador = 0
while contador < 10:
    print("Contando em:", contador)
    contador += 1

# Contador com valor informado pelo usuário
total = int(input("Quantas vezes contar? "))
contador = 1

while contador <= total:
    print(f"Contando: {contador}")
    contador += 1
