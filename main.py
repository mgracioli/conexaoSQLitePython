from usuario import Usuario
from crud import Crud

def main():
    crud = Crud()
    usuario = Usuario('Loiana','352352352','lo@luiza.com.br','36536536502')

    crud.inserir_dados(usuario)
    #crud.consultar_dados('Tuhanny')
    #crud.atualizar_dados('Tuhanny','Luiza')
    #crud.excluir_dados('Luiza')

    
main()