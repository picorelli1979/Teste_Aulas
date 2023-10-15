# 0, 1, 1, 2, 3, 5, 8
 
def f(n):
    
    if n == 1 :
      return 0
    
    if n == 2 :
        return 1
    
    return f(n-1) + f(n-2)

resp = int(input('QUAL A POSIÇÃO FIBONACCI DESTE NUMERO:  '))

print(f(resp))