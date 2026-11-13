import random

Nums = []

i = 0

while i < 30:
    Nums = Nums + [random.randint(1,100)]
    i = i + 1

print(Nums)

NumerosPares = 0
NumerosImpares = 0
NumerosSuperioresMedia = []

for n in Nums:
    if n % 2 == 0:
        NumerosPares = NumerosPares + 1
    else: 
        NumerosImpares = NumerosImpares + 1

    if n > (sum(Nums) / len(Nums)):
        NumerosSuperioresMedia.append(n)

print(NumerosPares)

print(NumerosImpares)

print(f"Maior Número: " , max(Nums))

print(f"Menor Número: " , min(Nums))

print(round(sum(Nums) / len(Nums), 2))

print(len(NumerosSuperioresMedia))

print(NumerosSuperioresMedia)

