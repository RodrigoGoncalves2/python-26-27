lista = []
for i in range(1,11):
    lista.append(i)

pares = [num for num in lista if num % 2 == 0]

print(pares)



quadrado = [num * num for num in lista]

print(quadrado)



palavras = ["Rodrigo", "Isabelly", "Davi", "Stasto"]

numletras = [len(palavra) for palavra in palavras]

print(numletras)



maior5 = [num for num in lista if num > 5]

print(maior5)



maior5 = [num for num in lista if num > 5]

print(maior5)

nome = "RoDrIgO"

nome.split()

letrasUpper = [letra for letra in nome if letra == letra.upper() and letra.isspace() == False]

print(letrasUpper)


numeros = [3, 6, 9, 12, 15, 10]

multi3 = [num * 2 for num in numeros if num % 3 == 0]

print(multi3)



nomes = ["Rodrigo", "Marcelo", "André", "Dinis", "Alberto"]

comecaA = [nome.upper() for nome in nomes if nome and nome[0].upper() == 'A']

print(comecaA)


frutas = ["Maçã", "Pera", "Banana", "Abacate", "Abacaxiwa"]

frutamais5 = [len(fruta) for fruta in frutas if len(fruta) > 5]

print(frutamais5)