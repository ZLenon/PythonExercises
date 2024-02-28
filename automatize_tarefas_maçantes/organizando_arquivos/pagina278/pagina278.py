from shutil import move


base = "./automatize_tarefas_maçantes/organizando_arquivos/pagina278/"

origem = base + "01/arquivo_movido.txt"


destino = base + "02/"

# move o arquivo se colocar um nome renomeia o arquivo
move(origem, destino)

# verificar a pasta 01 e 02 antes de executar esse arquivo
# as pastas que compõem o destino já devem existir; do contrário, o Python lançará uma exceção.
