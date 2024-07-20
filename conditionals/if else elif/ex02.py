minha_idade = int(input("Digite sua idade: "))

if minha_idade < 18:
    print("Sou menor de idade")
    
elif minha_idade > 18 and minha_idade <= 60:
    print("Sou adulto")

elif minha_idade > 60:
    print("Sou idoso")
    
    
else:
    print("Opção invalida")