def contar_vogais(str):
    return sum([1 for i in str if i in 'aeiouAEIOUáéíóúâêîôûãõÁÉÍÓÚÂÊÎÔÛÃÕ'])

frase = 'Oi, meu nome é Luann'

print(contar_vogais(frase))