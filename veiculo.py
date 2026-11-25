class Veiculos:
    def __init__(self,mat,marca,num_pneus=4):
        self.matricula = mat
        self.marca = marca
        self.num_pneus = num_pneus
    
@property
def matricula(self):
    return self.__matricula

@matricula.setter
def matricula(self,nova_matricula):
    self.__matricula = nova_matricula
    
class Moto(Veiculos):
    def __init__(self,matricula,marca,num_pneus,cilindrada):
        super().__init__(matricula,marca,num_pneus)
        self.cilindrada = cilindrada
        
    def __str__(self):
        return f"{self.matricula} - moto da marca {self.marca}"
    
    def __eq__(self,outra_moto):
        return self.marca == outra_moto.marca
    
    def fazer_barulho(self):
        print("bibibibibiibib")
            
v1 = Veiculos ("32-57-NT","Fiat")
v1.matricula = "33-22-XY"
print(v1.matricula)
v2 = Moto("11-11-AA","Kawasaki",2,1900)
v3 = Moto("12-11-AA","Kawasaki",2,1900)
v2.fazer_barulho()
print(v2)
if v2 == v3:
    print ("mesma marca")
    
# h = "HBO"
# x = HotelModel.query.filter_by(hotel=h).first()

x = "O alquimista;Paulo Coelho,1998;1"
lista = x.split(";")
print(lista)

