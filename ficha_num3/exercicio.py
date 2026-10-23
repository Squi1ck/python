
#pares = []
#for num in lista
#   if num % 2 == 0:
#       pares.append(num+1)
#   else:
#       pares.append

#pares = [num+1 if num < 5 else num for num in lista if num % 2 == 0]

#pares = [num for num in lista if num % 2 == 0]

lista=[1,2,3,4,5,6,7,8,9,10]
quadrados = [num**2 for num in lista]
print (quadrados)

palavras = ["Dinis","Carlos","Marcelo","Matias"]
tamanho_palavras = [len(palavra) for palavra in palavras]
print(tamanho_palavras)

nums_maior_5 = [num for num in lista if num > 5]
print (nums_maior_5)

maiusculas = "MarcelO ViEiRa amorIM"

letraMai = [letra for letra in maiusculas.insuper()]
print(letraMai)