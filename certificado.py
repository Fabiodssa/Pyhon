

numero1 = float(input("Digite o 1º numero: "))
numero2 = float(input("Digite o 2º numero: "))
numero3 = float(input("Digite o 3º numero: "))

if numero1 > numero2 and numero1 > numero3:  # Corrigido para comparar com numero3
    print("O maior numero é:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior numero é:", numero2)
else:
    print("O maior numero é:", numero3)