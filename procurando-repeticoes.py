n=str(input("Digite uma frase: ")).upper() .strip()
print ("seu sua frase tem {} letas A".format(n.count('A')))
print("parece na posição {} na primeira vez".format(n.find('A')+1))       
print("aparece pela ultima vez na posição {} " .format(n.rfind('A')+1)) 