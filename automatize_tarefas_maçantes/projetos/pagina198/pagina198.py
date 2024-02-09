# pagina198
PASSWORDS = {
    "email": "lenoninformatica@gmail.com",  # Senha para a conta de e-mail
    "blog": "www.otservelist.org",  # Senha para a conta do blog
    "senha": "Leonel1261@",  # Senha para a conta chamada "senha"
}
import sys, pyperclip  # Importação dos módulos necessários: sys para manipular argumentos da linha de comando e pyperclip para copiar para a área de transferência

if len(sys.argv) < 2:  # Verifica se não há argumentos suficientes
    print(
        "Usage: py pw.py [account] - copy account password"
    )  # Mensagem de uso caso não haja argumentos suficientes
    sys.exit()  # Encerra o script
account = sys.argv[1]  # O primeiro argumento da linha de comando é o nome da conta
if account in PASSWORDS:  # Verifica se a conta está presente no dicionário de senhas
    pyperclip.copy(
        PASSWORDS[account]
    )  # Copia a senha correspondente para a área de transferência
    print(
        "Password for " + account + " copied to clipboard."
    )  # Imprime uma mensagem indicando que a senha foi copiada com sucesso
else:  # Se a conta não está presente no dicionário de senhas
    print(
        "There is no account named " + account
    )  # Imprime uma mensagem indicando que não há nenhuma conta com o nome fornecido
