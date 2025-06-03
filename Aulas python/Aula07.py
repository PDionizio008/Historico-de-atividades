# X = 1

# while X <= 5:
#     print(X)
#     X = X + 1

# X = 1

# while X <= 100:
#     print(X)
#     X = X + 1


# X = 50

# while X <= 100:
#     print(X)
#     X = X + 1

# x = 10

# while x >=0:
#     print(x)
#     x = x - 1
# print("Lançamento do foguete autorizado!")

# x = 10

# while x <= 100:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1

# n = int(input("Escolha um número: "))

# x = 2

# while x <= n:
#      print(x)
#      x+= 2

import getpass

senha_correta = "senac"

while True:
    senha = getpass.getpass("Digite a senha para acessar o sistema: ")
    
    if senha == senha_correta:
        print("Login bem-sucedido! Bem-vindo ao sistema.")
        break
    else:
        print("Senha incorreta! Tente novamente.")

