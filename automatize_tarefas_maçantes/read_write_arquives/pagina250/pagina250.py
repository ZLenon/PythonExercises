from os import path

# retorna uma string com caminho absoluto
print(path.abspath("."))

# retorna um boleano TRUE se o caminho for absoluto e FALSE se for um caminho relativo
print(path.isabs("./automatize_tarefas_maçantes/read_write_arquives/pagina250"))

# retorna uma string contendo um path relativo ao primeiro parametro para o segundo paramentro.
print(path.relpath("/home", "./automatize_tarefas_maçantes"))
