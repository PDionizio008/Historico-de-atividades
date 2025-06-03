# soma = 0

# while True :
#     numero = float(input("Digite um numero para somar ou 0 para sair: "))
#     if numero == 0:
#        break
#     soma += numero 
# print(f"A soma de todos os numeros digitados é {soma}")

while True:
    idade = int(input("Digite uma idade: "))
    
    if idade >= 18:
        print("Acesso à festa concedido")
    else:
        print("Entrada proibida")

    while True:
        continuar = input("Deseja verificar mais alguma idade [S ou N]: ").strip().upper()
        if continuar == "S" or continuar == "N":
            break
        else:
            print("Opção inválida. Digite apenas 'S' ou 'N'.")
    
    if continuar == "N":
        break

print("Fim da verificação")

