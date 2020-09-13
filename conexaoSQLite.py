import sqlite3, time

class Conexao(object):

    def conectar(self):
        #cria o banco de dados e faz a conexão
        self._conexao = sqlite3.connect("bancoSQLite.db") #cria um banco de dados chamado bancoSQLite (está criando o banco  na pasta pythonProjects e não na pasta bancoMySQL não sei porque)

        self._cursor = self._conexao.cursor()

        #Cria uma tabela para o db
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS tabelabancoSQLite (nome TEXT NOT NULL,
                    telefone TEXT,
                    email TEXT,
                    CPF VARCHAR(11),
                    criado_em DATE);""")

    def desconectar(self):
        self._cursor.close()
        self._conexao.close()

    #getters e setters
    def get_cursor(self):
        return self._cursor

    def get_conexao(self):
        return self._conexao
        



    
    
