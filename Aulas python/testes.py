import time
import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII do foguete com fogo
foguete_fogo = r"""
       /\
      /  \
     / || \
    /  ||  \
   /   ||   \
  |    ||    |
  |    ||    |
  |    ||    |
  |    ||    |
 /|    ||    |\
/_|____||____|_\
   (        )
    (      )
     (____)
     |    |
     |    |
     |🔥🔥|
    /|🔥🔥|\
   /_|🔥🔥|_\
     /_/\
"""

# ASCII do foguete sem fogo (em voo ou descida)
foguete_voo = r"""
       /\
      /  \
     / || \
    /  ||  \
   /   ||   \
  |    ||    |
  |    ||    |
  |    ||    |
  |    ||    |
 /|    ||    |\
/_|____||____|_\
   (        )
    (      )
     (____)
     |    |
     |    |
     |    |
    /|    |\
   /_|____|_\
     /_/\
"""

# ASCII da explosão
explosao = r"""
        _.-^^---....,,--
    _--                  --_
   <                        >)
   |      BOOOOM!!!        |
   \._                   _./
      '''--. . , ; .--'''
            | |   |
         .-=||  | |=-.
         `-=#$%&%$#=-'
            | ;  :|
   _____.,-#%&$@%#&#~,._____
"""

# Contagem regressiva
x = 10
while x >= 0:
    limpar_tela()
    print(f"Contagem regressiva: {x}")
    time.sleep(1)
    x -= 1

limpar_tela()
print("🚀 Lançamento do foguete autorizado!")
time.sleep(2)

# Simula a decolagem com fogo
for i in range(5):
    limpar_tela()
    print(foguete_fogo)
    print("\nFoguete decolando...\n")
    time.sleep(0.7)

# Foguete voando
for i in range(3):
    limpar_tela()
    print(foguete_voo)
    print("\nFoguete em voo...\n")
    time.sleep(0.7)

# Explosão!
limpar_tela()
print(explosao)
print("\n💥 O foguete explodiu no ar! Missão fracassada. 😢\n")
time.sleep(3)

# (Opcional) Pouso forçado depois da explosão (versão cômica)
limpar_tela()
print(foguete_voo)
print("\n🪂 Parte do foguete caiu e está pousando de paraquedas...\n")
time.sleep(3)
print("🛬 Pouso de emergência realizado com sucesso (pelo menos uma peça se salvou)!\n")

