aluno = {
    "nome": "Carlos",
    "idade": 17,
    "cidade": "Famalicão",
    "disciplinas": ["Matemática", "Programação", "Inglês"],
    "notas": { "matematica": [17.5,12], "programacao": [18.25,13], "ingles": [12.25,7.75]}
} # Dicionário

# Imprimir o nome do aluno
print(aluno["nome"])

# Alterar o valor de uma chave
aluno["idade"] = 18

# Inserir uma nova chave
aluno["estado_civil"] = "Solteiro"

# Imprimir as caracteristicas do aluno
for chave in aluno.keys():
    print(f"{chave}", end = " ") 

print()

# Imprimir somente os valores
for valor in aluno.values():
    print(f"{valor}", end = " ")

print()

# Imprimir a chave e o valor
for chave,valor in aluno.items():
    print(f"{chave}: {valor}", end = "\n")

print()

# Adicionar uma disciplina
aluno["disciplinas"].append("Português")

# Imprimir as disciplinas
for disciplina in aluno["disciplinas"]:
    print(disciplina)

print()

# Imrpimir a segunda nota de programacao
print(aluno["notas"]["programacao"][1])

# Média de todas as notas
soma = 0
no_notas = 0
for notas_disciplina in aluno["notas"].values():
    soma += sum(notas_disciplina)
    no_notas += len(notas_disciplina)

print(f"A média das notas é: {round(soma/no_notas,2)}")