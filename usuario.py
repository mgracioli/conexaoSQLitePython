#cria um modelo de usuário

class Usuario(object):
    #método construtor
    def __init__(self, nome, telefone, email, cpf):
        self._nome = nome          #o _ informa que essa variável deve ser usada como se fosse private. Em python não existe variável privada, então, isso é só uma convenção para dizer que essa variável deve ser usada como se fosse private
        self._telefone = telefone  #o self deixa essa variável disponivel para uso dentro de todos os métodos dessa classe
        self._email = email        
        self._cpf = cpf
    
    
    @property
    def nome(self):
        return self._nome.title()   #.title() é para que o nome seja formatado com a primeira letra maiuscula. É um tratamento desse dado para que ele seja adicionado no banco de dados de forma correta, isso justifica o uso das @property

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email.lower()

    @property
    def cpf(self):
        return self._cpf
    