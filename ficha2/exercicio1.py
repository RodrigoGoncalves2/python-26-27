import os

tarefas = []
resposta = "S"

print(f"**Gestor De Tarefas**\n\n")

while resposta == "S":
    funcaoEscolhida = int(input((f"Quer utilizar o Gestor para que função?\n \t1- Adicionar Tarefa\n \t2- Adicionar Múltiplas Tarefas\n " \
    "\t3- Inserir Tarefa em Posição Específica\n \t4- Remover uma Tarefa pelo Nome\n " \
    "\t5- Remover Última Tarefa ou por Índice\n \t6- Remover todas as Tarefas \n " \
    "\t7- Contar Ocorrências de Tarefa\n \t8- Encontrar Índice de Tarefa\n \t9- Ordenar Tarefas\n " \
    "\t10- Inverter Ordem das Tarefas\n \t11- Copiar Lista de Tarefas\n \t12- Ver Lista de Tarefas\n")))

    match funcaoEscolhida:
        case 1:
            addTarefa = input("Que tarefa quer adicionar ao final da lista?: ")
            tarefas.append(addTarefa)
            print("\nLista Tarefas: " , tarefas , "\n")

        case 2:
            listaTarefas = input("O que quer adicionar à lista? (Informações separadas por ','): ")
            listaTarefas = listaTarefas.split(',')
            tarefas.extend(listaTarefas)
            print("\nLista Tarefas: " , tarefas , "\n")

        case 3:
            addTarefa = input("Que tarefa quer adicionar e em que posição colocar a tarefa? (Tarefa, Posição): ")
            addTarefa = addTarefa.split(", ")
            tarefa = addTarefa[0]
            posi = int(addTarefa[1])
            tarefas.insert(posi, tarefa)
            print("\nLista Tarefas: " , tarefas , "\n")

        case 4:
            print("\nLista Tarefas: " , tarefas , "\n")
            listaTarefas = tarefas
            removeu = False
            while listaTarefas == tarefas:
                remTarefa = input("Que tarefa quer remover? ")
                for tarefa in tarefas:
                    if remTarefa == tarefa:
                        tarefas.remove(tarefa)
                        removeu = True
                        print("Tarefa removida com sucesso!")
                if removeu == True:
                    break
                else:
                    print("Não existe essa tarefa!!!!\n")
            print("\nLista Tarefas: " , tarefas , "\n")
        case 5:
            print("\nLista Tarefas: " , tarefas , "\n")
            remUlt = input("Remover última tarefa = espaço(' '), remover posição específica = nº posição: ")
            if remUlt == " ":
                tarefas.pop()
            else:
                remUlt = int(remUlt)
                tarefas.pop(remUlt - 1)
            print("\nLista Tarefas: " , tarefas , "\n")
        case 6:
            print("\nLista Tarefas: " , tarefas , "\n")
            while len(tarefas) != 0:
                tarefas.pop()
            print("Todos os Elementos da Lista Removidos com Sucesso!!!")
            print("\nLista Tarefas Limpa: " , tarefas , "\n")

        case 7:
            print("\nLista Tarefas: " , tarefas , "\n")
            primeira
            print("A tarefa: " , ocoTarefa , " aparece " , ocorrência , " vezes.")
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
        case 12:
           print("Lista Tarefas: " , tarefas)
    resposta = (input(f"Deseja executar mais operações? (S/N)")).upper()
    if resposta == "N":
        print("Lista Tarefas: " , tarefas)
        break