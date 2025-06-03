# Criando Listas# Lista de estados
estados = ["TO", "SP", "RJ"]
estados.append("PA")  # adiciona item
estados.remove("SP")  # remove item
print(estados)        # ['TO', 'RJ', 'PA']

# Loop correto
for estado in estados:
    print(f"Olá, {estado}!")
