
# Lista de produtos
products = []

# Função para adicionar um produto
def add(nomeProduto="", preco=0.00, iva=0.23):
    p = {
        "product": nomeProduto,
        "price": preco,
        "tax": iva
    }
    products.append(p)
    return p


# Função para calcular o preço final
def update_final_price(dicionario_recebido):
    dicionario_recebido["final_price"] = round(dicionario_recebido["price"] *(1 + dicionario_recebido["tax"]), 2)


# Função para mostrar informações de um produto
def print_product(p):
    return f"O produto {p['product']} com o preço de {p['price']} e IVA de {p['tax']*100}%"


# Função para mostrar o menu
def menu():

    while True:

        funcaoEscolhida = input(
            "\n\n----- BEM VINDO AO MENU DE PRODUTOS -----\n\n"
            "QUE OPERAÇÕES QUER REALIZAR?\n"
            "1 - INSERIR UM NOVO PRODUTO\n"
            "2 - MOSTRAR TODOS OS PRODUTOS EXISTENTES\n"
            "3 - ATUALIZAR O PREÇO FINAL DE TODOS OS PRODUTOS\n"
            "4 - MOSTRAR OS DADOS DE UM PRODUTO ESPECÍFICO\n"
            "5 - TERMINAR A APLICAÇÃO\n"
        )

        match funcaoEscolhida:

            case "1":
                nomeproduto = input("QUAL É O NOME DO PRODUTO? ")
                precoproduto = input("QUAL É O PREÇO DO PRODUTO? ")
                taxaproduto = input("QUAL É A TAXA DE IVA? (EXEMPLO: 0.23) ")

                add(nomeproduto, float(precoproduto), float(taxaproduto))

                print("PRODUTO ADICIONADO COM SUCESSO!")

            case "2":
                if len(products) == 0:
                    print("NÃO EXISTEM PRODUTOS!")
                else:
                    for i, produto in enumerate(products):
                        print(f"PRODUTO {i + 1}: {produto}")

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

