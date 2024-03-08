import os, re

datePattern = re.compile(
    r"""^(.*?) # todo o texto antes da data
((0|1)?\d)- # um ou dois dígitos para o mês
((0|1|2|3)?\d)- # um ou dois dígitos para o dia
((19|20)\d\d) # quatro dígitos para o ano
(.*?)$ # todo o texto após a data
""",
    re.VERBOSE,
)
path = "./automatize_tarefas_maçantes/projetos/pagina287/"

for file_name in os.listdir(path):
    mo = datePattern.search(file_name)
    print(file_name)
    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    print("Antes: ", beforePart)
    print("Depois: ", afterPart)
    print("Mes: ", monthPart)
    print("Dia: ", dayPart)
    print("Ano: ", yearPart)
    # Renomeando ao padrao europeu
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
    print("Nome padrão EUA: ", euroFilename)

    # Caminho dos arquivos que serao mudados o nomes
    old_dir_name = os.path.join(path, file_name)
    new_dir_name = os.path.join(path, euroFilename)
    print("Caminho: ", new_dir_name)
    os.rename(old_dir_name, new_dir_name)
    print("=*" * 20)
