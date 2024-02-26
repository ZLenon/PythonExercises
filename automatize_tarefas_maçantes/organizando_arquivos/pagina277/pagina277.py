from shutil import copy, copytree

origem = "./codigo_cores.py"

destino = "./automatize_tarefas_maçantes/organizando_arquivos/pagina277/"

# Copia o arquivo de um local para outro
copy(origem, destino)

# ------------------------------------------

# Copia um pasta de um local para outro o utmimo nome apos a utima barra é necessario /backup
origem_two = "./automatize_tarefas_maçantes/tratamento_erros"
destino_two = "./automatize_tarefas_maçantes/organizando_arquivos/pagina277/backup"
copytree(origem_two, destino_two)
