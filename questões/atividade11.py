def retornar_acima_media(lista):
    return sum([1 for nota in lista if nota > 5])

notas = [9,7,8,4,3,6,2,1]

print(retornar_acima_media(notas))