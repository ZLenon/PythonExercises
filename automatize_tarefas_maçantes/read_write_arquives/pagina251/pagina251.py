from os import path

caminho_mock = (
    "./automatize_tarefas_maçantes/read_write_arquives/pagina251/pagina251.py"
)
# O nome base está depois da última barra em um path e corresponde ao nome do arquivo
y = path.basename(caminho_mock)
print(y)

# O nome do diretório corresponde a tudo que estiver antes da última barra
x = path.dirname(caminho_mock)
print(x)

# returna uma tupla dividindo em duas strings
z = path.split(caminho_mock)
print(z)
