import os

tarefas = []
tarefasVarias = []
resposta = "S"
resposta2 = "S"

print(f"Gestor De Tarefas\n\n")

while resposta == "S":
    funcaoEscolhida = int(input((f"Quer utilizar o Gestor para que função?\n \t1- Adicionar Tarefa\n \t2- Adicionar Múltiplas Tarefas\n " \
    "\t3- Inserir Tarefa em Posição Específica\n \t4- Remover uma Tarefa pelo Nome\n " \
    "\t5- Remover Última Tarefa ou por Índice\n \t6- Remover todas as Tarefas \n " \
    "\t7- Contar Ocorrências de Tarefa\n \t8- Encontrar Índice de Tarefa\n \t9- Ordenar Tarefas\n " \
    "\t10- Inverter Ordem das Tarefas\n \t11- Copiar Lista de Tarefas:\n")))

    match funcaoEscolhida:
        case 1:
            addTarefa = input("Que tarefa quer adicionar ao final da lista?")
            tarefas.append({addTarefa})
        case 2:
            while resposta2 == "S":
                resposta2 = (input("Quer adicionar várias tarefas ao mesmo tempo? (S/N)")).upper()
                if resposta2 == "S":
                    addTarefa = input("Que tarefa quer adicionar à lista?")
                    tarefasVarias = tarefas
                    tarefasVarias.append({addTarefa})
                    resposta2 = (input("Quer adicionar mais tarefas(S/N)")).upper()

    resposta = (input(f"Quer executar mais operações? (S/N)")).upper()
    if resposta == "N":
        mostrarLista = (input("Quer ver a lista? (S/N)")).upper()
        if mostrarLista == "S":
            print(tarefas)
        # case 3:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 4:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 5:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 6:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 7:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 8:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 9:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 10:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})
        # case 11:
        #     addTarefa = input("Que tarefa quer adicionar ao final da lista?")
        #     tarefas.append({addTarefa})