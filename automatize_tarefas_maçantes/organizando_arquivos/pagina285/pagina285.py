from zipfile import ZipFile


base = "./automatize_tarefas_maçantes/organizando_arquivos/pagina285/"

arquivo = base + "pixel_art.zip"
# ----------------------------------------------------------
info_zip = ZipFile(arquivo)  # le o arquivo zip

# info_zip.extractall(path=base + "/data")  # extaia para o local

# ----------------------------------------------------------
info_zip.extract("civil.png", path=base + "/data")  # extrai somente 1 arquivo do zip


info_zip.close()  # fecha o arquivo
