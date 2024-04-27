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
  classe = exercicio10.Metodos_String("")
  metodo = classe.string_format_map({'nome': 'João', 'idade': 30})
  assert metodo == 'Alo'