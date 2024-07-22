notas = []

for i in range(3):
    codigo_aluno = input("Seu RM: ")
    nome = input("Digite seu nome: ")
    nota = float(input("Sua note: "))
    
    resutado = [codigo_aluno, nome, nota]
    notas.append(resutado)
    


for x in notas:
  
    codigo_aluno = x[0]
    aluno = x[1]
    nota = x[2]
    
    print(f"O aluno {aluno} do codigo {codigo_aluno} teve uma nota de {nota}")
    
    
