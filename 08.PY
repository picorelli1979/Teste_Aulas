
lista = [1,2,3,4,5,6,7,-1,-5,-9,-11,-13,-27]

# DESTA FORMA É LISTCOMPRESHION:
#lista_impares =[ x for x in lista if x % 2 == 1 ]

for impares in lista:
    if impares % 2 == 1:
        print(impares, end= '/')    
