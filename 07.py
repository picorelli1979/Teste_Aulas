# FUNÇÃO DENTRO DE FUNÇÃO 

def gerar_potencia(pot):
    def potencia(base):
        return base ** pot
    return potencia

quadrado = gerar_potencia(2)
cubico = gerar_potencia(3)

print(quadrado(78))
print(cubico(3))