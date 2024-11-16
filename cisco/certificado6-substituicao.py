# Suponha que a lista tenha 5 elementos
lista = [10, 20, 30, 40, 50]

# Etapa 1: Substituir o número do meio por um número inserido pelo usuário
lista[len(lista) // 2] = int(input("Digite um número inteiro para substituir o número do meio: "))

# Etapa 2: Remover o último elemento da lista
del lista[-1]

# Etapa 3: Imprimir o comprimento da lista
print(len(lista))
print(lista)