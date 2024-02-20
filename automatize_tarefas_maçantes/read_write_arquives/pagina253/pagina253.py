from os import path

caminho = "./automatize_tarefas_maçantes/read_write_arquives/pagina253/pagina253.py"

# retorna true se o arquivo ou pasta existir
print("Caminho Existe: ", "Sim" if path.exists(caminho) else "Não")

# retorna true se existir e for um arquivo
print("Caminho é um arquivo: ", "Sim" if path.isfile(caminho) else "Não")

# retorna true se existir e for uma pasta
print("Caminho é uma pasta: ", "Sim" if path.isdir(caminho) else "Não")
