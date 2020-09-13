import sqlite3, time

class Conexao(object):

    def conectar(self):
        #cria o banco de dados e faz a conexão
        self._conexao = sqlite3.connect("bancoSQLite.db") #cria um banco de dados chamado bancoSQLite

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

"""
def inserir_dados(nome, tel, ema, cpf):
    data = time.strftime("%d/%m/%Y")
    c.execute("INSERT INTO tabelabancoSQLite VALUES (?, ?, ?, ?, ?)", (nome, tel, ema, cpf, data))
    connect.commit() #commita as infos no banco de dados
    print("\nSalvando informações no db...")
    time.sleep(1.5)

def consultar_dados(nome_consultar):
    sql = "SELECT * FROM tabelabancoSQLite WHERE nome = ?"
    for linha in c.execute(sql, (nome_consultar,)):
        print("")
        print ("Nome: ",linha[0])
        print ("Telefone: ",linha[1])
        print ("E-mail: ",linha[2])
        print ("CPF: ",linha[3])
        print ("Data de cadastro: ",linha[4])


def atualizar_dados(novo, antigo):
    c.execute ("UPDATE tabelabancoSQLite SET nome = ? WHERE nome = ?", (novo, antigo))
    connect.commit()

continua = True

while continua == True:
    opcao = input("\n\nO que deseja fazer?:\n1 - Cadastrar funcionário\n2 - Pesquisar funcionário\n3 - Atualizar funcionário\n4 - Excluir funcionário\n5 - Sair\n")

    if (opcao == '1'):
        print("\n\n::::....CADASTRAR FUNCIONÁRIO....::::")
        print("")

        nome = input("Insira o nome: ")
        tel = input("Insira o telefone: ")
        ema = input("Insira o email: ")
        cpf = input("Insira o CPF: ")

        try:
            inserir_dados(nome, tel, ema, cpf)
        except:
            print("\nErro ao cadastrar")
        else:
            print("\nCadastro realizado com sucesso")

    elif opcao == '2':
        print("\n\n::::....PESQUISAR FUNCIONÁRIO....::::")
        print("")

        try:
            nome_consultar = input("Insira o nome: ")
            consultar_dados(nome_consultar)
        except:
            print("\nFuncionário não localizado")

    elif opcao == '3':
        print("\n\n::::....ATUALIZAR FUNCIONÁRIO....::::")
        print("")

        antigo = input("Insira o nome antigo: ")
        novo = input("Insira o novo nome: ")

        atualizar_dados(novo, antigo)
        
    elif opcao == '4':
        print("nao implementado ainda")

    elif opcao == '5':
        continua = False
        print("\n\nFinalizando programa...")
"""





    
    
