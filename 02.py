
print('=======================O NUMERO MAIOR=============================================')
def num_maior(num1, num2):  
    num1=int(input('DIGITE O PRIMEIRO NUMERO:   '))
    print('='*50)
    num2=int(input('DIGITE O SEGUNDO NUMERO:    '))
    print('='*50)
    
    if num1 > num2 :
        print(f'O PRIMEIRO NUMERO {num1} é maior que O SEGUNDO NUMERO {num2}')
    elif num2 > num1 :
        print(f'O SEGUNDO NUMERO {num2} é maior que PRIMEIRO NUMERO {num1}')   
    else: 
        print(f'O PRIMEIRO NUMERO {num1} e SEGUNDO NUMERO {num2} SÃO IGUAIS ')  
             
num_maior(100,40)

print('=================================================================================')








