#cria um modelo de usuário

class Usuario(object):
    #método construtor
    def __init__(self, nome, telefone, email, cpf):
        self._nome = nome          #o _ informa que essa variável deve ser usada como se fosse private. Em python não existe variável privada, então, isso é só uma convenção para dizer que essa variável deve ser usada como se fosse private
        self._telefone = telefone  #o self deixa essa variável disponivel para uso dentro de todos os métodos dessa classe
        self._email = email        
        self._cpf = cpf

    #inicio dos getters
    def get_nome(self):
        return self._nome
    
    def get_telefone(self):
        return self._telefone

    def get_email(self):
        return self._email

    def get_cpf(self):
        return self._cpf