my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)

# Inicialmente, largest = 17 (o primeiro número da lista).
# O laço começa com i = 3 (segundo número da lista):
# 3 > 17 → falso, então largest permanece 17.
# Em seguida, i = 11:
# 11 > 17 → falso, então largest permanece 17.
# Depois, i = 5:
# 5 > 17 → falso, então largest permanece 17.
# E assim por diante até o final da lista.
# Quando o loop terminar, largest terá o valor 17, pois é o maior número da lista.