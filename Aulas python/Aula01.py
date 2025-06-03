faturamento = 1500
custo = 700
imposto = 0.1 * faturamento
lucro = faturamento - custo - imposto
#manipulando string
#print(faturamento)
#print(custo)
#print(imposto)
#print(lucro)

#print(f"O faturamento é {faturamento} , custo é {custo} o imposto é {imposto} e lucro é {lucro}")

#print("O faturamento é {}, custo é {} o imposto é {} e lucro é {}".format(faturamento, custo, imposto, lucro))

email_cliente = "Dionizioo@king.net.com"
#Colocando todas as letras maiusculas
email_cliente =email_cliente.upper()
print(email_cliente)
#colocando todas as letras minusculas
email_cliente = email_cliente.lower()
print(email_cliente)

nome_cliente = "pedro Dionizio"
#colocando primeira letra do nome maiusculo
nome_cliente = nome_cliente.capitalize()
print(nome_cliente)

#Colocando as primeiras letras do nome em maiusculo
nome_cliente = nome_cliente.title()
print(nome_cliente)

#Encontar caracter no texto
print(nome_cliente.find("i"))
print(email_cliente.find("@"))

#Contar quantas caracteres tem no texto
print(len(nome_cliente))
print(len(email_cliente))

#Pegar um caracter
print(nome_cliente[13])

#Pegar um pedaço do texto
print(email_cliente[1:4])

# Subatituir parte do texto
email_cliente = email_cliente.replace("@king.net.com","@gmail.com")
print(email_cliente)

#Dividir texto
email = "qualquercoisa@gmail.com"
provedor = email.split("@")[1]
print("O p´rovedor do email é", provedor)

nome = "Pedro Henrique Alves Dionizio de Santana"
nome1= nome.split()[1]
print(nome1)
