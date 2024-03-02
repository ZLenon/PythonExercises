from zipfile import ZipFile


base = "./automatize_tarefas_maçantes/organizando_arquivos/pagina284/"

arquivo = base + "pixel_art.zip"
# ----------------------------------------------------------

# faz a leitura dos arquivos contidos no zip
file_zip = ZipFile(arquivo)
print(file_zip.namelist())  # Nomes

# Pega a informação de 1 arquivo
info_one_zip = file_zip.getinfo("janus.png")

print("Arquivo Normal: " + str(info_one_zip.file_size) + " kbps")

print("Arquivo zipado: " + str(info_one_zip.compress_size) + " kbps")

# fecha o processo de leitura
file_zip.close()
