from os import walk

base = "./automatize_tarefas_maçantes/organizando_arquivos"

for pastas_principais in walk(base):
    print(pastas_principais[0])
