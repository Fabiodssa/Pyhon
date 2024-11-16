drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]

 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

# drawn = [5, 11, 9, 42, 3, 49]
# Aqui é definida a lista drawn com os números sorteados.

# bets = [3, 7, 11, 42, 34, 49]
# Esta é a lista bets, que contém os números apostados.

# hits = 0
# A variável hits é inicializada com o valor 0. Ela vai contar quantos números apostados aparecem na lista dos sorteados.

# for number in bets:
# Este loop percorre cada elemento da lista bets (números apostados).

# if number in drawn:
# Dentro do loop, para cada número number da lista bets, é verificado se ele existe na lista drawn 
# (ou seja, se o número apostado foi sorteado).

# hits += 1
# Se o número apostado estiver presente na lista dos sorteados (if number in drawn), 
# então a variável hits é incrementada em 1.

# print(hits)
# Finalmente, após o loop, o código imprime o valor da variável hits, que é o número total de acertos 
# (quantos números apostados coincidem com os sorteados). 