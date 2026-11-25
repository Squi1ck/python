class Livro:
    def __init__(self,titulo,autor,ano,estado="disponivel"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano
        self.estado = estado
        
        def __str__(self):
            return f"{self.titulo} {self.autor} ({self.ano_publicado}) [{self.estado}]"
        
        def emprestar(self):
            if self.estado == "disponivel":
                self.estado = "emprestados"
                return True
            return False
                
        def devolver(self):
            self.estado = "Disponivel"