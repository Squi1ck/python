import random

nums = []

i = 0
while i <= 29:
    nums.append(random.randint(1,100))
    i = i + 1
print (nums)

s= sum(nums)
maior=max(nums)
menor=min(nums)
media= s / len(nums)

pares = 0
impares = 0
acima_media = 0
lista_acima_media = []

# Para cada num da minha lista
# Se o nº for maior que a media
    #  Aumenta dew 1 a variável acima_media
    # Coloca o num na lista lista_acima_media

for n in nums:
    if n > media:
        acima_media = acima_media+1
        lista_acima_media.append(n)
    
print (n)
