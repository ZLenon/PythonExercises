from os import path, listdir

# retorna uma lista com os nomes dos arquivos locais
print(listdir("."))

# retorna em bytes o tamanho do arquivo
print(path.getsize("."), " bytes")

# ---------------------------------------------------
total_file = 0
for file_name in listdir("."):
    total_file += path.getsize(file_name)
    print(path.getsize(file_name), " bytes", file_name)

print(total_file)
