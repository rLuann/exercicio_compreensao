def gerar_lista_tamanho(lista):
    return [(palavra, len(palavra)) for palavra in lista]

entrada = ["python", "java", "javascript", "c"]
resultado = gerar_lista_tamanho(entrada)

for palavra, tamanho in resultado:
    print(f"O tamanho da palavra {palavra} é: {tamanho}")