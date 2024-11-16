import random
# print("o numero sorteado foi: {}".format(random.randint(1,10)))

# n1=input("Digite o nome: ")
# n2=input("Digite o nome: ")
# n3=input("Digite o nome: ")
# n4=input("digite o nome: ")
# l=[n1,n2,n3,n4]
# print("O escolhido foi: {}".format(random.choice(l)))

n1=str(input("digite o nome: "))
n2=str(input("digite o nome: "))
n3=str(input("digite o nome: "))
n4=str(input("digite o nome: "))
l=[n1,n2,n3,n4]
random.shuffle(l)
print("a ordem sera: {}".format(l))