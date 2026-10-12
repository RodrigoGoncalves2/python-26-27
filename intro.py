# Pare por cada letra de uma palavra e indique o nº de vogais da mesma
texto = "Marcelo VIeira Amorim"
num_vogais = 0
for letra in texto:
    if letra.upper() in "AEIOU":
        num_vogais = num_vogais + 1
print(num_vogais)


lista = texto.slip(" ")
print(lista)

