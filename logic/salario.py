meu_salario = int(input("Informe seu salario: "))

if meu_salario <= 3000:
    print("Progamador Junior")


elif meu_salario >= 300 and meu_salario < 6000:
    print("progamdor pleno")
    
elif meu_salario >= 6000 and meu_salario <= 20000:
    print("Progamador Senior")
    
else:
    print("CEO")