# criando um dicionario 
banco_dados = {  
    'nome' : 'FABRICIO PAIM',
    'cargo': 'DEV. JUNIOR',
    'email': 'fabricio001devenloper@gmail.com', 
    'salario' : 'R$ 8.000,00' ,
    'Alpha' : 'id_key'    
}

banco_dados['idade'] = 44  # criando uma chave dentro do dicionario
banco_dados['telefone'] = 9818171726727 # criando uma chave dentro do dicionario

print(banco_dados.get('Alpha', 'NÃO EXISTE TAL DETERMINAÇÃO'))

banco_dados.update([['Musica', 'Fernandinho']])
# usando o update atualizamos o dicionario com um par de chaves e inserimos os elementos 
print(banco_dados)

elemento = banco_dados.get('nome')
print(elemento)