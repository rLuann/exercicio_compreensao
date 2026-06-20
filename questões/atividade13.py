def retornar_pares_matriz(matriz):
    return [numero for linha in matriz for numero in linha if numero % 2 == 0]

matriz = [[1,2,3], [4,5,6], [7,8,9]]

print(retornar_pares_matriz(matriz))