from exercicios import exercicio10

def test_captalize():
  classe = exercicio10.Metodos_String("lENON NAScimento")
  metodo = classe.string_capitalize()
  # Primeira letra em maiusculo
  assert metodo == "Lenon nascimento"

def test_casefold():
  classe = exercicio10.Metodos_String("LENON NASCIMENTO")
  metodo = classe.string_casefold()
  # Tudo em minusculo
  assert metodo == 'lenon nascimento'

def test_center():
  classe = exercicio10.Metodos_String('Lenon')
  metodo = classe.string_center()
  # Add caracteres antes e depois
  assert metodo == "=======Lenon========"

def test_count():
  classe = exercicio10.Metodos_String("O rato roeu a roupa do rei de roma")
  metodo = classe.string_count('r')
  # retorna o numero de vezes de uma ocorrencia em uma string
  assert metodo == 5

def test_endswith():
  classe = exercicio10.Metodos_String("www.google.com")
  metodo = classe.string_endswith('.com')
  # retorna boleano
  assert metodo == True

def test_expandtabs():
  classe = exercicio10.Metodos_String('L\te\tn\to\tn')
  metodo = classe.string_expandtabs(2)
  # cria um espaço quando for usado o \t de tabulação
  assert metodo == 'L e n o n'

def test_find():
  classe = exercicio10.Metodos_String('Ordem e Progresso')
  metodo = classe.string_find('Progresso')
  # retorn o index inicial da string informada, case sensitive
  assert metodo == 8

def test_format():
  classe = exercicio10.Metodos_String("Meu nome é: ")
  metodo = classe.string_format("Lenon")
  assert metodo == "Meu nome é: Lenon"

def test_format_map():
  classe = exercicio10.Metodos_String('Olá, meu nome é {nome} e tenho {idade} anos.')
  metodo = classe.string_format_map({'nome': 'Lenon', 'idade': 34})
  assert metodo == 'Olá, meu nome é Lenon e tenho 34 anos.'

def test_index():
  classe = exercicio10.Metodos_String('LenonNascimentoCardoso')
  metodo = classe.string_index('Nasci')
  assert metodo == 5

def test_isalnum():
  classe = exercicio10.Metodos_String('Lenon2024')
  metodo = classe.string_isalnum()
  # Retorna verdadeiro se todos os caracters da string forem Alfanumericos
  assert metodo == True

def test_isalpha():
  classe = exercicio10.Metodos_String('Nascimento')
  metodo = classe.string_isalpha()
  # Retorna verdadeiro se todos os caracter forem letras
  assert metodo == True

def test_isascii():
  classe = exercicio10.Metodos_String('abc123#$%')
  metodo = classe.string_isascii()
  # Retorna verdadeiro se todos os caracters forem ascii
  assert metodo == True

def test_isdecimal():
  classe = exercicio10.Metodos_String("987654231")
  metodo = classe.string_isdecimal()
  # Retorna verdadeiro se os caracters forem numerais
  assert metodo == True

def test_isdigit():
  classe = exercicio10.Metodos_String('  ')
  metodo = classe.string_isdigit()
  # Retorna verdadeiro se nao houver caracters nulos
  assert metodo == False

def test_isidentifier():
  classe = exercicio10.Metodos_String('abc123')
  metodo = classe.string_isidentifier()
  # Válido se contiver apenas letras alfanuméricas (az) e (0-9) ou sublinhados (_). Um identificador válido não pode começar com um número ou conter espaços.
  assert metodo == True

def test_islower():
  classe = exercicio10.Metodos_String('abcdfg')
  metodo = classe.string_islower()
  # confere se as letras estao em lowercase
  assert metodo == True

def test_isnumeric():
  classe = exercicio10.Metodos_String('98754321')
  metodo = classe.string_isnumeric()
  # Retorna verdadeiro se todos caracters forem numeros
  assert metodo == True

def test_isprintable():
  classe = exercicio10.Metodos_String('teste123')
  metodo = classe.string_isprintable()
  # método retorna True se todos os caracteres puderem ser impressos, caso contrário, False.
  assert metodo == True

def test_isspace():
  classe = exercicio10.Metodos_String("  $  ")
  metodo = classe.string_isspace()
  # retorna true se todos os caracters forem espaço
  assert metodo == False

def test_istitle():
  classe = exercicio10.Metodos_String('Lenon Nascimento')
  metodo = classe.string_istitle()
  # Retorna verdadeiro se todas as palavras começar com maiusculo
  assert metodo == True

def test_isupper():
  classe = exercicio10.Metodos_String('TESTANDO')
  metodo = classe.string_isupper()
  # Retorna verdadeiro se todas as letras forem maiuscula
  assert metodo == True

def test_join():
  classe = exercicio10.Metodos_String('-')
  metodo = classe.string_join(('Lenon','Nascimento','Cardoso'))
  # método pega todos os itens em um iterável e os une em uma string.
  assert metodo == 'Lenon-Nascimento-Cardoso'

def test_ljust():
  classe = exercicio10.Metodos_String('Lenon')
  metodo = classe.string_ljust(10)
  # Retorne uma versão justificada à esquerda com x caracter da palavra
  assert metodo == 'Lenon     '

def test_lower():
  classe = exercicio10.Metodos_String("CAPSLOCK")
  metodo = classe.string_lower()
  assert metodo == 'capslock'

def test_lstrip():
  classe = exercicio10.Metodos_String("!@#$%¨&*Lenon")
  metodo = classe.string_lstrip("&*¨%#@!$")
  assert metodo == "Lenon"