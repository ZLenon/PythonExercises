from os import unlink, rmdir, listdir

base = "./automatize_tarefas_maçantes/organizando_arquivos/pagina280/"

arquivo = base + "01/test.txt"


pasta = base + "02/"

# Apaga o arquivo no caminho indicado
# unlink(arquivo)
# ------------------------------------------------------

# Apaga a pasta indicada no caminho
# rmdir(pasta)
# ------------------------------------------------------

# Apaga um arquivo especifico de uma forma mais segura
# for filename in listdir(path=base + "/01"):
#     if filename.endswith(".rxt"):
#         print(f"O arquivo {filename} foi deletado")
#         unlink(base + "/01/" + filename)
