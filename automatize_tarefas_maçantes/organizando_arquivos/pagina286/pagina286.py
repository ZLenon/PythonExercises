from zipfile import ZipFile, ZIP_DEFLATED

base = "./automatize_tarefas_maçantes/organizando_arquivos/pagina286/"

arquivo = base + "pixel_art.zip"

with ZipFile(arquivo, "w") as file:
    file.write("spam.txt", compress_type=ZIP_DEFLATED)
