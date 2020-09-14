from usuario import Usuario
from crud import Crud

def main():
    crud = Crud()
    usuario = Usuario('ToniNhA','352352352','lo@LuIZa.com.Br','36536536502')

    crud.inserir_dados(usuario)
    #crud.consultar_dados('Tuhanny')
    #crud.atualizar_dados('Tuhanny','Luiza')
    #crud.excluir_dados('Luiza')

    
main()
