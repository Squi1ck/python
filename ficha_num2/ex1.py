# Cenário

# O formando será responsável por desenvolver um programa que permite ao utiliza-
# dor gerir uma lista de tarefas. O programa deverá suportar as seguintes funcionali-
# dades, utilizando os métodos de lista apropriados:

# 1. Adicionar Tarefa: Adicionar uma nova tarefa ao final da lista.
# 2. Adicionar Múltiplas Tarefas: Adicionar várias tarefas de uma vez.

# 3. Inserir Tarefa em Posição Específica: Adicionar uma tarefa numa posição espe-
# cífica da lista.

# 4. Remover Tarefa por Nome: Remover uma tarefa específica da lista pelo seu con-
# teúdo.

# 5. Remover Última Tarefa ou por Índice: Remover a última tarefa ou uma tarefa
# numa posição específica.

# 6. Remover todas as Tarefas: Remover todas as tarefas da lista.
# 7. Contar Ocorrências de Tarefa: Verificar quantas vezes uma tarefa específica
# aparece na lista.
# 8. Encontrar Índice de Tarefa: Localizar a primeira ocorrência de uma tarefa na
# lista.
# 9. Ordenar Tarefas: Organizar as tarefas em ordem alfabética.
# 10. Inverter Ordem das Tarefas: Reverter a ordem atual das tarefas.
# 11. Copiar Lista de Tarefas: Criar uma cópia independente da lista de tarefas.

tarefas=[]

tarefas.append(1)
tarefas.extend([2,3,4])
tarefas.insert(3,1)
# tarefas.pop()
# tarefas.remove(3)
# tarefas.clear()
print(tarefas.count(1))
print(tarefas)
primeira_ocorrencia=tarefas.index(1)
print(primeira_ocorrencia)
tarefas.sort()
tarefas.sort(reverse=True)
tarefa2=tarefas.copy()

print(tarefas)
print(tarefa2)
