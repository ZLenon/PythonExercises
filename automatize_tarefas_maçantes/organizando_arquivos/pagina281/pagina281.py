from send2trash import send2trash
from time import sleep

base = "./automatize_tarefas_maçantes/organizando_arquivos/pagina281/"

arquivo = base + "bacon.txt"
# ----------------------------------------------
baconFile = open(arquivo, "a")  # cria o arquivo
baconFile.write("Bacon is not a vegetable.")
baconFile.close()
# ---------------------------------------------
print(sleep(5), flush=True)  # espera 5 seg
# -------------------------------------------
send2trash(arquivo)
# Apaga o arquivo criado
