# Versão com compreensão:
def achatar(lista):
    return [item for elemento in lista for item in (achatar(elemento) if isinstance(elemento, list) else [elemento])]

lista = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]

print(achatar(lista))

# Versão sem compreensão:
'''def achatar(lista):
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(achatar(elemento))
        else:
            resultado.append(elemento)
    return resultado

lista = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]
print(achatar(lista)) ''' 