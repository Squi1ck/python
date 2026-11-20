# Criar o dicionário aluno
aluno = {
    "Nome": "Ana Silva",
    "Idade": 17,
    "Disciplinas": ["Matemática", "Física", "Informática"],
    "Notas": {
        "Matemática": 18,
        "Física": 17,
        "Informática": 19
    }
}

# 1. Adicionar uma nova disciplina e respetiva nota
aluno["Disciplinas"].append("Português")
aluno["Notas"]["Português"] = 16

# 2. Modificar a idade para 18
aluno["Idade"] = 18

# 3. Imprimir todas as disciplinas e respetivas notas
for disciplina, nota in aluno["Notas"].items():
    print(disciplina, ":", nota)

# 4. Calcular e imprimir a média das notas
media = sum(aluno["Notas"].values()) / len(aluno["Notas"])

print("Média das notas:", media)