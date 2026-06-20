def filtrarNomes(lista):
    return [palavra for palavra in lista if len(palavra) > 5 ]


nomes = ['Luann', 'Michel', 'Rocha', 'Moura', 'Aragão', 'Santana', 'Sócrates']

print(filtrarNomes(nomes))