def retornar_valores_positivos(lista):
    return [i for i in lista if i >0]

lista = [-2,-5,-4,2,5,4,7,8,9,-7,-9,12,-12]

print(retornar_valores_positivos(lista))