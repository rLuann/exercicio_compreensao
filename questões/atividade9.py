def eh_primo(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True

def definir_primos(n):
    return [x for x in range(1,n) if eh_primo(x)]

n = int(input())

print(definir_primos(n))
