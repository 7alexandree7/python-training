idade = int(input("Sua idade: "))
cnh = input("Voce Possui CNH? ")

if (idade >= 18 and cnh == "True"):
    print(f"voce tem {idade} e possui cnh")
    
elif (idade > 18 or cnh != "True"):
    print(f"voce é maior de idade, porem não tem cnh")
    
else:
    print("Não tem idade suficiente nem possui carteira de motoristas")