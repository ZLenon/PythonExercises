import os

try:
    result = os.getcwd()
    print(result)
    os.chdir("/home/local/inexistente")
    result = os.getcwd()
    print(result)
except FileNotFoundError:
    print("Local inexistente, coloque um local valido")
