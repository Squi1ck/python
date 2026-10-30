quadrados = {str(i): i*i for i in range (1,11)}
print(quadrados)

palavras = ["alicate","dados","parlamento","python","ficionario"]
dic_palavras = {palavra: len(palavra) for palavra in palavras}
print(dic_palavras)

notas = {"Ana": 18, "bruno": 15,"carla":17,"david":12,"eva":19}
melhores_alunos = {aluno: nota for aluno,nota in notas.items() if nota > 15} 
print(melhores_alunos)