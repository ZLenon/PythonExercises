tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(param=list):
    for index, lista in enumerate(tableData):
        for x in lista:
            print(index, x)


printTable(tableData)
