class Cliente:
    def __int__(self,nome,peso,altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        Cliente.total_clientes
        
    def __str__(self):
        return (f"O cliente{c1.nome} tem {c1.altura}cm e pesa{c1.peso} kg")
    
    def __eq__(self, value):
        return self.nome == c1.nome
        
c1 = Cliente("Ana",62,1.67)
c2 = Cliente("Ana",71,1.71)
c3 = Cliente("Alberto",67,1.90)

#metodo da classe
@Classmethod
def procurar(cls,cliente_a_pesquisar):
    if cliente_a_pesquisar == "Ana":
        return True 
    return False

lista = [c1,c2,c3]

if c1 == c2:
    print ("ok")
if c2 == c3:
    print ("segundo ok")

print (f"Total de cliente: {Cliente.total_clientes}")

for c in lista:
    if Cliente.procurar(c.nome):
        print(c)
