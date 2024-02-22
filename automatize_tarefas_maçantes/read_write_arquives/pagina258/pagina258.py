path = "./automatize_tarefas_maçantes/read_write_arquives/pagina258/infos.txt"


data = open(path, "w")
# Escrita
print(data.write("lenon\n"))
data.write("Hello world!\n")
data.write("Bacon is not a vegetable.\n")
data.close()

# leitura
data = open(path, "r")
infos = data.read()
data.close()

print(infos)
