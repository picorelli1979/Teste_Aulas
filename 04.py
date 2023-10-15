# LISTA VAZIA  

lista = []

# CRIEIE UM FOR COM RANGE E COM 10 NUMEROS PARA GERAR UMA LISTA 

for num in range (10):
    lista.append(int(input('DIGITE OS NUMEROS:   ')))

print('='*30)
print(f'OS NUMEROS DIGITADOS NO TERMINAL FORAM :{lista}')
print('='*30)
print(f'A SOMATORIA DOS NUMEROS DIGITADOS NO TERMINAL FOI: {sum(lista)}')   
print('='*30)

# FUNÇÃO CRIADA PARA TIRAR A MÉDIA DA LISTA 

def media_lista():   
    media = sum(lista)/len(lista)
    return media

print(f'A MÉDIA DA LISTA ACIMA FOI {media_lista()}')
print('='*30)