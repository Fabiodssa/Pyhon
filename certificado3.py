c=0
nu=[]
while c<5:
    n=float(input("DIgite um numero: "))
    nu.append(n) ## O número inserido pelo usuário é adicionado ao final da lista nu usando o método append(). Isso faz com que cada número inserido seja colocado na lista de forma sequencial.
    c+=1

mr=max(nu)
print("o maior é:",mr)
