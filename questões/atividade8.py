def definir_pares(lista):
    return [x for x in lista if x % 2 == 0]

numeros = [0,1,2,3,4,5,6,7,8,9]

print(definir_pares(numeros))