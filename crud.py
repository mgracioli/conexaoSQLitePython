
from  conexaoSQLite import Conexao
from usuario import Usuario
import time

class Crud(object):

    def __init__(self):
        try:
            self.con = Conexao()

            self.con.conectar()
            self.conexao = self.con.get_conexao()
            self.cursor = self.con.get_cursor()
        except Exception as e:
            print('Erro ao fazer a conexão pelo crud')
            print(e)

    def inserir_dados(self, usuario):
        try:
            data = time.strftime("%d/%m/%Y")
            self.cursor.execute("INSERT INTO tabelabancoSQLite VALUES (?, ?, ?, ?, ?)", (usuario.get_nome(), usuario.get_telefone(), usuario.get_email(), usuario.get_cpf(), data, ))
            self.conexao.commit() #commita as infos no banco de dados
        except Exception as e:
            print('\nErro ao inserir usuário')
            print(e)
        else:
            print("\nUsuário salvo com sucesso")
        finally:
            self.con.desconectar()

    def consultar_dados(self, nome):
        try:
            sql = "SELECT * FROM tabelabancoSQLite WHERE nome = ?"
            
            for linha in self.cursor.execute(sql, (nome,)):
                print("")
                print ("Nome: ",linha[0])
                print ("Telefone: ",linha[1])
                print ("E-mail: ",linha[2])
                print ("CPF: ",linha[3])
                print ("Data de cadastro: ",linha[4])
        except Exception as e:
            print('\nUsuário não localizado')
            print(e)
        finally:
            self.con.desconectar()

    def atualizar_dados(self, nome_antigo, novo_nome):
        try:
            self.cursor.execute ("UPDATE tabelabancoSQLite SET nome = ? WHERE nome = ?", (nome_antigo, novo_nome, ))
            self.conexao.commit()
        except Exception as e:
            print('\nNão foi possível atualizar os dados do usuário')
            print(e)
        finally:
            self.con.desconectar()