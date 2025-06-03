# Usando operadores matemáticos
#print(1+1)
#print(10-1)
#print(100/20)
#print(1500*4)

'''
pra poder comentar varias linhas clica nas asapas simples 3 vezes, devendo conter 6 aspas
'''

# Aspas Simples
#print ("Pedro Henrique Dionizio")
#print(1, "Pedro")
#print(123456789)
#print (2, "Pedro ' Dionizio'")
#print ("Pedro \"Dionizio\"")

#Tipos de int 
print(11)
print(-11)
print(0)

#Float
print(1.1, 10.11)
print(0.0, -1.5)

#Tipo de dados
print(type('Pedro Henrique'))
print(type(0))
print(type(1.1))
print (type(2025-4-15))

#comparadores lôgicos
print(10 == 20)#False
print(10 == 10)#true
print(type(True))
print(type(False))

#str, int, float, bool
print(int('1'), type(int('1')))
print(type (float('1') + 1))
print (bool (' '))
print (str(11) + 'b')

#Criando Variaveis
nome = 'Pedro Henrique'
soma = 2+2+2+2+2+2+2+2
idade = 18
maior_idade = idade >=18
data_nascimento = ("28/1/2005")
print(nome)
print(soma)
print(soma + soma)
print('nome:', nome, 'idade', idade)
print('É maior?', maior_idade)
print(nome,'Tem',idade,'anos','nasceu em:',data_nascimento)

nome = input ("Digite o seu nome completo: ")
idade = int(input("Digite a sua Idade :"))
altura = float (input("Digite a sua altura:"))
resposta = input("Você está matriculado em algum curso? (sim/não): ")
matriculado = resposta.lower() in ["sim", "s"]
matriculado = resposta.lower() in ["não", "n"]

print("\n--- DADOS CADASTRADOS ---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:} m")
print(f"Matriculado: {matriculado}")

if matriculado:
       print("Status:Matriculado em um curso")
else:
       print("Status:Não Matriculado em um curso")