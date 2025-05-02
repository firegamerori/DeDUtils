import random

def roll(dado: str):
    soma = 0
    local_soma = dado.find("+")
    somas = dado[local_soma+1:].split("+")
    
    if local_soma == -1:
        local_soma = len(dado)
    else:
        for i in somas:
            soma += int(i)
    
    lista_dados = dado[0:local_soma].split("&")


    for i in lista_dados:
        r = i.split("d")
        quantidade = r[0]
        valor = r[1]
        for x in range(0, int(quantidade)):
            soma += random.randint(0, int(valor))
    

    return soma
