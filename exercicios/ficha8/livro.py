livro = {}

with open("livros.txt", "r", encoding="utf-8") as f:
    i = 1
    for linha in f:
        palavras = linha.strip().split(";")
        nome = palavras[0]
        autor = palavras[1]
        ano = palavras[2]
        emprestado = palavras[3]
        chave = f"livro{i}"
        livro[chave] = palavras
        i = i + 1      

class Livro:
    def __init__(self, nome, autor, ano, emprestado=1):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.emprestado = emprestado

    def emprestar():
        estado = "Disponível"
        for n in livro:           
            if livro[n][3] == 1:
                estado = "Emprestado"
                livro[n][3] = 0
        return estado

    
    def devolver(estado):
        for n in livro:
            if livro[n][3] == 1:
                estado = "Emprestado"
                livro[n][3] = 0
            elif livro[n][3] == 0:
                estado = "Disponível"
                livro[n][3] = 1

        return estado

    def __str__(estado):
        return f"{self.nome} - {self.autor} ({self.ano}) [{estado}]."

    


