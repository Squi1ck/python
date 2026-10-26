aluno = {
            "nome": "Ana Silva",
            "idade": 17,
            "disciplinas": ["Matemática", "Física", "Informática"],
            "notas": {
                "Matemática": 18,
                "Física": 16,
                "Informática": 15
            }
        }
aluno["notas"]["portugues"] = 16
aluno["disciplinas"].append("Português")

aluno["idade"] = 18

for disciplinas , notas in aluno["notas"].items():
    print(disciplinas, notas)

notas_aluno = []
for nota in aluno["notas"].values():
    notas_aluno.append(nota)
    media = round(sum(notas_aluno)/len(notas_aluno),2)

print (media)


resultado = contar_caracteres