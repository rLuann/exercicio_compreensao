def retornar_letras(lista):
    return [letra for palavra in lista for letra in palavra]

entrada = ["python", "java"]
print(retornar_letras(entrada))