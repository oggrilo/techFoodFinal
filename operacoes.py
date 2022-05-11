import mysql.connector
import conexao
import menuLogin

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserirCliente(nomeCliente, cpfCliente, celularCliente, senhaCliente):
    try:
        sql = "insert into cliente(codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente) values('','{}','{}','{}','{}')".format(nomeCliente, cpfCliente, celularCliente, senhaCliente)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)

#Consultar os dados do BD
def selecionarCliente():
    try:
        sql = "select * from cliente"
        con.execute(sql)

        for (codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente) in con:
            print(codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente)
        print('\n')
    except Exception as erro:
        print(erro)

#Atualizar dados no banco de dados
def atualizarNomeCliente(codigoCliente, nomeCliente):
    try:
        sql = "update cliente set nomeCliente = '{}' where codigoCliente = '{}'".format(nomeCliente,codigoCliente)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Nome do cliente, Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarCelularCliente(codigoCliente, celularCliente):
    try:
        sql = "update cliente set celularCliente = '{}' where codigoCliente = '{}'".format(celularCliente,codigoCliente)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Celular do cliente, Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarSenhaCliente(codigoCliente, senhaCliente):
    try:
        sql = "update cliente set senhaCliente = '{}' where codigo = '{}'".format(senhaCliente,codigoCliente)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Senha do Cliente, Atualizada!")
    except Exception as erro:
        print(erro)

def excluirCliente(codigoCliente):
    try:
        sql = "delete from cliente where codigo = '{}'".format(codigoCliente)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, codigoCliente + "Deletada!")
    except Exception as erro:
        print(erro)

def loginCliente(cpfCliente,senhaCliente):
    try:
        sql = "select * from cliente = '{}' where cpfCliente and senhaCliente = '{}'".format(cpfCliente,senhaCliente)
        con.execute(sql)

        for (cpfCliente, senhaCliente) in con:
            print(cpfCliente, senhaCliente)
        print('\n')
    except Exception as erro:
        print(erro)

