from zipfile import ZipFile

with ZipFile("new.zip", "w") as file:
    file.write("spam.txt", compress_type=ZipFile.ZIP_DEFLATED)
