# 1ª Parte

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



aluno["disciplinas"].append("Português")

aluno["notas"]["Português"] = 16



aluno["idade"] = 18



for disciplina, nota in aluno["notas"].items():
    print(disciplina, nota)



media = sum(aluno["notas"].values()) / len(aluno["notas"])

print(media)



# 2ª Parte

def contar_caracteres(texto):
    frequencia = {}

    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

    return frequencia

print(contar_caracteres("Marcelo"))



# 3ª Parte

biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

for livro in biblioteca.values():
    if livro["disponivel"] == True:
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



# 4ª Parte
quadrados = {str(n): n * n for n in range(1,11)}


palavras = ["Rodrigo", "Ana", "Maçã", "Pera", "Isabelly"]

comprimento = {palavra: len(palavra) for palavra in palavras}

notas = {
    "Ana": 18,
    "Bruno": 15,
    "Carla": 17,
    "David": 12,
    "Eva": 19
}

notasMais15 = {nome: nota for nome, nota in notas.items() if nota >= 15}

print(notasMais15)
