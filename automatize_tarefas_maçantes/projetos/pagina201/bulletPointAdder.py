import pyperclip

# Obter texto da área de transferência
text = pyperclip.paste()

# Dividir o texto em linhas
lines = text.splitlines()

# Adicionar "*" no início de cada linha
lines = ["* " + line for line in lines]

# Juntar as linhas de volta em um único texto
modified_text = "\n".join(lines)

# Copiar o texto modificado para a área de transferência
pyperclip.copy(modified_text)
