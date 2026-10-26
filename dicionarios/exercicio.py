aluno = {
    "nome": "Ana Silva",
    "idade": 17,
    "disciplinas": ["Matemática", "Física", "Informática"],
    "notas": {
        "Matemática": 18,
        "Física": 17,
        "Informática": 19
    }
}


aluno["notas"]["Português"] = 16
aluno["disciplinas"].append("Português")

aluno["idade"] = 18

for disciplina, nota in aluno["notas"].items():
    print(disciplina, nota)


media = sum(aluno["notas"].values()) / len(aluno["notas"])

print("Média: ", media)


def contarCaracteres(texto):
    frequencia = {}


    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

    return frequencia

print(contarCaracteres("banana"))



biblioteca = {
    "livro1": {
        "titulo": "Python",
        "autor": "Luciano Ramalho",
        "disponivel": True
    },
    "livro2": {
        "titulo": "Matemática   ",
        "autor": "Ana Silva",
        "disponivel": True
    },
    "livro3": {
        "titulo": "Fluent Python",
        "autor": "Luciano Ramalho",
        "disponivel": True
    }
}


for livro in biblioteca.values():
    if livro["disponivel"]:
        print(livro["titulo"])


biblioteca["livro4"] = {
    "titulo": "A saga do Gonçalves",
    "autor": "Rodrigo Gonçalves",
    "disponivel": True
}

biblioteca["livro1"]["disponivel"] = False




titulos = []

for livro in biblioteca.values():
    if livro["autor"] == "Luciano Ramalho":
        titulos.append(livro["titulo"])


print(titulos)


exercicio4 = {n: n * n for n in range(1,11)}
print(exercicio4)


palavras = ["Programação", "Jogos", "Vídeo", "Rodrigo", "Maçã", "Porta"]

palavraChave = {palavra: len(palavra) for palavra in palavras}

print(palavraChave)


notas = {
    "Ana": 18,
    "Bruno": 15,
    "Carla": 17,
    "David": 12,
    "Eva": 19
}


notasmais15 = {nome: nota for nome, nota in notas.items() if nota >= 15}