nome=input("digite seu nome: ") .strip() ## retira os espaços do inicio e do final do nome
print(nome.upper())
print(nome.lower())
print(len(''.join(nome.split())))
print(nome.find(' '))