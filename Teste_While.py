contador = 0

while contador < 10:
    print(contador)
    contador = contador + 1
    if contador == 11:
        print('Objetivo Alcaçando')  
        break
else:
    print('Objetivo....realizado!!! Você esta fora do laço')    
    