f = open("exercicios/ficheiros/dados.txt", "r")
lista = f.readlines()

for linha in lista:
    print(linha.strip())

f.close()


with open("exercicios/ficheiros/dados.txt","r") as f:
    lista = f.readlines()
    for linha in lista:
        print(linha.strip())


with open("exercicios/ficheiros/nomes.txt", "w") as file:
    file.write("Marcelo\n")
    file.write("Ana\n")