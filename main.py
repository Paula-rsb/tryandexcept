import time
def abre_arquivo ():
    try:
        arquivo = open ('arquivoteste.txt')
        return True
    except Exception as erro:
        print ('Algo deu errado:', erro)
        return False
while not abre_arquivo():
    print ('Tentando encontrar o arquivo')
    time.sleep(5)

print ('Arquivo encontrado:')


