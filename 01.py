def nota_aluno(nota1, nota2):
    media = (nota1 + nota2) / 2
    situação = 'APROVADO' if media > 6.5 else 'REPROVADO'
    
    return media, situação
    
print(nota_aluno(5.5, 5.0))

    