nota1=float(input("Digite a primeira: "))
nota2=float(input("Digite a segunda "))
nota3=float(input("Digite a terceira "))
media=(nota1+nota2+nota3)/3
print("APROVADO" if media>=6 else "RECUMPERAÇÂO", "media: {:.2f}" .format(media)) #condição simplificada
#if media<6.0:
#    print("RECUMPERAÇÂO \n media: {:.2f}" .format(media))
#else:
#     print("APROVADO \n media: {:.2f}" .format(media))