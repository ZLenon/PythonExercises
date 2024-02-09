# pagina 179


def displayInventory(item=dict):
    print("Inventario:")
    for k, v in item.items():
        print(f"{v}-{k}")
    print(f"Total de items: {sum(item.values())}")


itens = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

displayInventory(itens)
