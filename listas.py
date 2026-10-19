nums = [2,5,8,11,7,9,13]

# Imprimir a lista
print(nums) # [2,5,8,11,7,9,13]

# Imprimir um elemento da lista
print(nums[2]) # 8

# Inserir um novo elemento no final da lista
nums.append(17) # [2,5,8,11,7,9,13,17]

# Inserir vários elementos no final da lista
nums.extend([12,16]) # [2,5,8,11,7,9,13,17,12,16]

# Inserir em posição específica
nums.insert(3,29) # [2,5,8,29,11,7,9,13,17,12,16]

# Remover o elemento no final da lista
nums.pop() # [2,5,8,29,11,7,9,13,17,12]

# Remover um elemento de uma posição especifíca da lista pelo índice
nums.pop(2) # [2,5,29,11,7,9,13,17,12]

# Remover um elemento de uma posição especifíca da lista pelo valor
nums.remove(17) # [2,5,29,11,7,9,13,12]

# Nº de elementos da lista
total = len(nums) # 8

# Para cada elemento da lista <= 10
for n in nums:
    if n <= 10:
        print(n, " ")

# Para percorrer por indice
for indice in range(len(nums)):
    if nums[indice] <= 10:
        print(nums[indice], end= " ")


nums2 = nums
nums.append(2)
print(nums, nums2)

nums3 = nums2.copy() # As listas são independentes
nums2.append(1000)
print(nums2, nums3)

# Ordenar
nums.sort

jogadores.index("J3") # 3
# ["J1","J2","J9","J3","J5","J7"]
jogadores.append("J5")
#numero de ocorrencias
jogadores.acount("J5")

#LIST COMPRENSION
#nums = []
#for i in range(1,101)
#   nums.append(i)
nums=[i for i in range (1,101)]
nums2=[8,11,5,3,21,19,14,7]
#nums filtrados = []
#for num in nums2
#   if 10 <= num <= 20:
#       nums_filtrados.append(num)

nums_filtrados = [num for num in nums2 if 10<= num <=20]

nums_filtrados2 = []
for num in nums2:
    if 10 <= num <= 20:
        nums_filtrados.append(num)
    if num % 2 == 0:  # é par
        nums_filtrados2.append(num*2)
    else: 
        nums_filtrados2.append(num)
        #[11,28,19]
nums_filtrados3 = [num*2 if num % 2 == 0 else num for num in nums2 if 10 <= num <=20]

print(nums_filtrados3)

frutas = ["morango","banana","ameixa","pera"]
#numero de caracteres de cada fruta
letras_frutas =[len(frutas) for fruta in frutas]
print(letras_frutas)

nome = "marcelo"
print (nome)
nome = list(nome)
print(nome)

lista = ["AI","Mar","Abr"]
novos_elementos = input ("Novos dados")
lista.extend(novos_elementos.split(','))
print(lista)