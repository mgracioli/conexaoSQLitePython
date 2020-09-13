
from usuario import Usuario
from crud import Crud

def main():
    crud = Crud()
    usuario = Usuario('Luiza','352352352','lu@luiza.com.br','36536536502')

    crud.inserir_dados(usuario)
    #crud.consultar_dados('ana')
    
main()