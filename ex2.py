import random

nums = []

i = 0
while i <= 14:
    nums.append(random.randint(0,20))
    i = i + 1
print (nums)


s= sum(nums)
maior=max(nums)
menor=min(nums)
media= s / len(nums)
aprovados = 0
reprovados = 0
num_alunos_16 = 0
percentagem_aprovados = 0
acima_media = 0
lista_acima_media = []

for n in nums:
    if n >=10 :
        aprovados = aprovados+1
    else :
        reprovados = reprovados+1
    if n >= 16 :
        num_alunos_16 = num_alunos_16+1
    if n > media:
        acima_media = acima_media + 1
        lista_acima_media.append(n)
        
    percentagem_aprovados = (aprovados / len(nums)) * 100
    
print(f"alunos aprovados{aprovados}")
print(f"alunos reprovados{reprovados}")
print(f"alunos com 16 ou mais{num_alunos_16}")
print(f"maior nota{maior}")
print(f"menor nota{menor}")
print(f"media turma: {round(media,2)}")
print(f"percentagem turma{round(percentagem_aprovados,2)}")

