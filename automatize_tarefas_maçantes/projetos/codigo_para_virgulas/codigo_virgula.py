# pagina 126


def lista_compras(lista=list):
    for x in lista:
        str(x).replace("\n", ",")
        print(x, end=",")


spam = ["apples", "bananas", "tofu", "cats", "grapes", "orange"]
lista_compras(spam)
