produtos = ["ABC123", "abd012", " ABS111", "AbB222"]

def tratar_texto (texto):
    
    texto = texto.upper()
    texto = texto.strip()
    
    return texto

for indicie, produto in enumerate(produtos):
    
    produtos[indicie] = tratar_texto (produto)

    
print(produtos)
