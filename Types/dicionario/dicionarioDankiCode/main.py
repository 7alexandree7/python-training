dicionario = {"nome": "alexandre", "idade": 22, "logico": True, "numeroFloat": 5.5}

print(type(dicionario))
print(dicionario)

# Acessar e imprimir os valores do dicionário
for chave in dicionario:
    print(f"chave: {chave} Valor: {dicionario[chave]}")