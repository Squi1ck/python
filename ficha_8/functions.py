from livro import Livro

def carregar_livros(nome_ficheiro):
    with open (nome_ficheiro,"r") as f:
        linhas = f.readlines()
    lista_livros = []
    for lin in linhas:
        linhas = lin.split(";")
        if lin[3].strip() == "0":
            estado = "emprestado"
        else:
            estado = "disponivel"
        livro = Livro(linhas[0],linhas[1],int(linhas[2]),estado)
        lista_livros.append(livro)
    return lista_livros
                    
                    
teste = carregar_livros("dados/livros.txt")
for livro in teste:
    print (livro)