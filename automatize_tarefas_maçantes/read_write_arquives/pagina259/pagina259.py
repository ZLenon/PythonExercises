import shelve

path = "./automatize_tarefas_maçantes/read_write_arquives/pagina259/data_binary"

with shelve.open(path) as db:
    db["Nome"] = "Lenon"
    db["Age"] = 34


with shelve.open(path) as db:
    print(db["Nome"])
    print(db["Age"])
