lista=[10,20,30,40,50,60,70,80,90,100]
#lista[len(lista)//2]=int(input("diigite um valor: "))
#print(lista)
lista.insert(4,900)
print(lista)

#A função insert() é usada para inserir um valor em uma lista em uma posição específica. 
# O método insert(índice, valor) insere o valor fornecido no índice especificado.
# Aqui, insert(0, i + 1) insere o valor i + 1 no índice 0 da lista, ou seja, no início da lista.
# O valor i + 1 é inserido em cada iteração, com i variando de 0 a 4.
# Isso faz com que os valores 1, 2, 3, 4 e 5 sejam inseridos, mas sempre na frente da lista,
# empurrando os elementos anteriores para a direita.