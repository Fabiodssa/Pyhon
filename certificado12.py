WHITE_PAWN = "♙"  # Definindo o símbolo do peão branco (Unicode)
row = []

for i in range(8):
    row.append(WHITE_PAWN)

print(row)

###################

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "dias estavam quentes.")