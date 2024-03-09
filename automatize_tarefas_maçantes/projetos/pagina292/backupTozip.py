import os, zipfile

path = "./automatize_tarefas_maçantes/projetos/pagina292/"


def backupToZip(param):
    folder = os.path.abspath(param)
    number = 1

    while True:
        zipFileName = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFileName):
            break

    number += 1
    print("Criando!!! " + zipFileName)
    backupZip = zipfile.ZipFile(zipFileName, "w")
    # ----------------------------------------------
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % (foldername))
        # Acrescenta a pasta atual ao arquivo ZIP.
        backupZip.write(foldername)

        # Acrescenta todos os arquivos dessa pasta ao arquivo ZIP.
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue  # não faz backup dos arquivos ZIP de backup
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print("Criado com sucesso! ")


backupToZip(path)
