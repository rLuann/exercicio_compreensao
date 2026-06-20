def definir_primos(n):
    return [x for x in range(1,n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))  if x > 1]

n = int(input())

print(definir_primos(n))
