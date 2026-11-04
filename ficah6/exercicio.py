inventario = []

def adicionarItem(id, titulo, autor, quantidade, preco):    
    livro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
        float("preco"): preco
    }
    inventario.append(livro)
    return livro

def mostrarInv():
    i = 0
    for item in inventario:
        print(f"PRODUTO {i + 1}- ID: {inventario[item]["id"]}\nTÍTULO: {inventario[item]["titulo"]}\nAUTOR: {inventario[item]["autor"]}\nQUANTIDADE NO STOCK: {inventario[item]["quantidade"]}\n")
        i = i + 1

def menu():

    while True:

        funcaoEscolhida = input(
            "\n\n----- BEM VINDO AO INVENTÁRIO DA BIBLIOTECA -----\n\n"
            "QUE OPERAÇÕES QUER REALIZAR?\n"
            "1 - VER INVENTÁRIO\n"
            "2 - ADICIONAR ITEM\n"
            "3 - ATUALIZAR STOCK\n"
            "4 - REMOVER ITEM\n"
            "5 - PRESQUISA AVANÇADA\n"
            "6 - RELATÓRIO DE STOCK\n"
        )

        match funcaoEscolhida:

            case "1":
                if len(inventario) == 0:
                    print("NÃO EXISTEM LIVROS!")
                else:
                    mostrarInv()

            case "2":
                idnovo = max(livro["id"] for livro in inventario) + 1
                nomelivro = input("QUAL É O TÍTULO DO LIVRO? ")
                autorlivro = input("QUAL É O AUTOR DO LIVRO? ")
                quantidadestock = input("QUAL É A QUANTIDADE DE UNIDADE EM STOCK? ")
                precolivro = input("QUAL É O PREÇO DO LIVRO? ")

                adicionarItem(idnovo, nomelivro, autorlivro, quantidadestock, float(precolivro))

                print("LIVRO ADICIONADO COM SUCESSO!")

            case "3":
                for produto in products:
                    update_final_price(produto)

                print("PREÇOS ATUALIZADOS COM SUCESSO!")

            case "4":
                produtoescolhido = input(
                    "QUER VER AS INFORMAÇÕES DE QUE PRODUTO? "
                )

                encontrado = False

                for produto in products:
                    if produtoescolhido == produto["product"]:
                        print(print_product(produto))

                        if "final_price" in produto:
                            print(f"PREÇO FINAL: {produto['final_price']}")

                        encontrado = True
                        break

                if encontrado == False:
                    print("PRODUTO NÃO ENCONTRADO!")

                voltar = input("DESEJA VOLTAR AO MENU? (S/N): ").upper()

                if voltar == "N":
                    print("A TERMINAR A APLICAÇÃO...")
                    break

            case "5":
                print("A TERMINAR A APLICAÇÃO...")
                break

            case _:
                print("OPÇÃO INVÁLIDA!")