lista_1 = [ num for num in range (1,10,)] # metodo list comprehension

lista_1.append([20,30,40,50]) # adiciona um valor final a sequencia 

lista_1.clear() # desta forma apagamos o conteudo 

lista_1 = ['a', 'b', 'c']

lista_2 = lista_1.copy() # aqui faz uma copia da lista original 

print(lista_1)
print(lista_2)

lista_2.extend(['z', 'x', 'w', 'l']) # aqui ele intera a lista com os interaveis que passar 

print(lista_2)

lista_2.insert(5,'Fabricio') #colocamos o elemnto aonde queremos passando o indice para ele

print(lista_2)

lista_2.pop(5) # aqui removemos o elemento desejado passando o indice 

letra_removida = lista_2.pop(5)

print(lista_2)

print(letra_removida)

print(lista_1)  # aqui estamos com uma lista a aplicamos uma condição e demos o REMOVE

if 'Z' in lista_1:
    lista_1.remove('Z') # o REMOVE ele dá a opção de TRUE and FALSE 
else:
    print('Não encontrei o Z')
    
print(lista_2)

lista_2.reverse() # aqui apenas ele traz a lista de forma reversa 

print(lista_2)   

lista_3 = [ 'Vin Diesel', 'Paul Walker', 'Aquaman', 'Micael', 'Kalleo']

lista_3.sort() # nesse metodo organizamos a lista em ordem alfabetica 

list(enumerate(lista_3)) # aqui ele devolve o objeto enumerado 

print(lista_3)

for indice, lista_3 in list(enumerate(lista_3)): # fazemos um for e damos enumerate para indexar
    print(indice, lista_3)
   
    


 





