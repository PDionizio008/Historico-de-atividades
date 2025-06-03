# def saudação_pedro():
#     print('OLÁ, PEDRO')
#     print('TEM 10 CELULARES NO ESTOQUE') 


# def saudação_joaquim():
#     print('OLÁ, JOAQUIM')
#     print('TEM 8 CELULARES NO ESTOQUE')


# def saudação_antonio():
#     print('OLÁ, ANTONIO')
#     print('TEM 5 CELULARES NO ESTOQUE')

# saudação_pedro()
# saudação_joaquim()
# saudação_antonio()

# def somar_numeros():
#     num1 = 10
#     num2 = 20
#     resultado = num1 + num2
#     print(resultado)

# somar_numeros()

# def somar_numeros2():
#     num1 = 5
#     num2 = 5
#     resultado = num1 + num2
#     print(resultado)

# somar_numeros()
# somar_numeros2()


# def somar(a,b):
#     resultado = a + b
#     print(resultado)

# somar(5,20)


# def saudação(nome,quantidade):
#     print(f'Olá, {nome}')
#     print(f'Temos {int(quantidade)} celulares no estoque')

# saudação('Pedro',10)
# saudação('Joaquim',8)
# saudação('Antonio',6)

# crie uma função chamada dobro que receba um número
# e retorne o dobro desse número.

# def dobro(numero):
#     return numero * 2 

# print(dobro(5))   # Saída: 10
# print(dobro(3.5)) # Saída: 7.0


# faça uma função que calcule a media das 4 notas de um aluno.


def calcular_media():
    print("Digite as 4 notas do aluno:")
    try:
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        n4 = float(input("Nota 4: "))
        return (n1 + n2 + n3 + n4) / 4
    except ValueError:
        return "Por favor, insira valores numéricos válidos."

# Chamando a função e mostrando o resultado
media = calcular_media()
print(f"A média do aluno é: {media}")


