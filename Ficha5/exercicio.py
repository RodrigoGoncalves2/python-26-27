products = []

nomeProduto = ""
preco = 0
iva = 0

def add(nomeProduto, preco, iva):
    dicionario = {
        "product": nomeProduto, 
        "price": preco, 
        "tax": iva
    }

    products.append(dicionario)

def novaChave():
    dicionario["final_price"] = 