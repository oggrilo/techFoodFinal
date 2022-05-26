import mysql.connector
import conexao
import menuADM
import crudFuncionario
import menuLogin

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserirCliente(nomeCliente, cpfCliente, celularCliente, senhaCliente):
    try:
        sql = "insert into cliente(codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente) values('','{}','{}','{}','{}')".format(nomeCliente, cpfCliente, celularCliente, senhaCliente)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, " Cliente Cadastrado! ")
    except Exception as erro:
        print(erro)

def inserirFunc(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc):
    try:
        sql = "insert into funcionario(codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) values('','{}','{}','{}','{}','{}')".format(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, " Funcionário Inserido! ")
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

def selecionarFunc():
    try:
        sql = "select * from funcionario"
        con.execute(sql)

        for (codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) in con:
            print(codigoFunc, nomeFunc, cpfFunc, celularFunc,salarioFunc, senhaFunc)
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

def atualizarNomeFunc(codigoFunc, nomeFunc):
    try:
        sql = "update funcionario set nomeFunc = '{}' where codigoFunc = '{}'".format(nomeFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Nome do Funcionário, Atualizado!")
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

def atualizarCelularFunc(codigoFunc, celularFunc):
    try:
        sql = "update funcionario set celularFunc = '{}' where codigoFunc = '{}'".format(celularFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Celular do funcionário, Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarSenhaCliente(codigoCliente, senhaCliente):
    try:
        sql = "update cliente set senhaCliente = '{}' where codigoCliente = '{}'".format(senhaCliente,codigoCliente)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Senha do Cliente, Atualizada!")
    except Exception as erro:
        print(erro)

def atualizarSenhaFunc(codigoFunc, senhaFunc):
    try:
        sql = "update funcionario set senhaFunc = '{}' where codigoFunc = '{}'".format(senhaFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Senha do funcionário, Atualizada!")
    except Exception as erro:
        print(erro)


def atualizarSalario(codigoFunc, salarioFunc):
    try:
        sql = "update funcionario set salarioFunc = '{}' where codigoFunc = '{}'".format(salarioFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Salário do funcionário, atualizado, novo salario: " + salarioFunc + "$")
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


def excluirFunc(codigoFunc):
    try:
        sql = "delete from funcionario where codigoFunc = '{}'".format(codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, codigoFunc + "Deletada!")
    except Exception as erro:
        print(erro)

def loginCliente(cpfCliente,senhaCliente):
    try:
            sql = "select * from cliente where cpfCliente = '{}' and senhaCliente = '{}'".format(cpfCliente,senhaCliente)
            con.execute(sql)

            for (cpfCliente, senhaCliente) in con:
                print(cpfCliente, senhaCliente)
            print('Logado como CLIENTE!!!\n')
    except Exception as erro:
        print(erro)
def loginFunc(cpfFunc,senhaFunc):
    try:
        sql = "select * from funcionario where cpfFunc = '{}' and senhaFunc = '{}'".format(cpfFunc, senhaFunc)
        con.execute(sql)

        for (codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) in con:
            print(cpfFunc, senhaFunc)
        print('Logado como FUNCIONÁRIO!!!\n')
        return menuADM.operacao()
    except Exception as erro:
        print(erro)


        #PARTE DOS LANCHES ---->
def inserir(nomeLanche, descricaoLanche, valorLanche, quantidadeLanche):
    try:
        sql = "insert into pessoa(codigoLanche, nomeLanche, descricaoLanche, valorLanche, quantidadeLanche) values('','{}','{}','{}', '{}')".format(nomeLanche, descricaoLanche, valorLanche, quantidadeLanche)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)

#Consultar os dados do BD
def selecionar():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        for (nomeLanche, descricaoLanche, valorLanche, quantidadeLanche) in con:
            print(nomeLanche, descricaoLanche, valorLanche, quantidadeLanche)
        print('\n')
    except Exception as erro:
        print(erro)

def selecionarValor():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        for (valorLanche) in con:
            print(valorLanche)
        print('\n')
    except Exception as erro:
        print(erro)

def selecionarQuantidade():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        for (quantidadeLanche) in con:
            print(quantidadeLanche)
        print('\n')
    except Exception as erro:
        print(erro)

#Atualizar dados no banco de dados
def atualizarNome(codigoLanche, nomeLanche):
    try:
        sql = "update lanche set nomeLanche = '{}' where codigoLanche = '{}'".format(nomeLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarDescricao(codigoLanche, descricaoLanche):
    try:
        sql = "update lanche set descricaoLanche = '{}' where codigoLanche = '{}'".format(descricaoLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarValor(codigoLanche, valorLanche):
    try:
        sql = "update lanche set valorLanche = '{}' where codigoLanche = '{}'".format(valorLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarQuantidade(codigoLanche, quantidadeLanche):
    try:
        sql = "update lanche set quantidadeLanche = '{}' where codigoLanche = '{}'".format(quantidadeLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def excluir(codigoLanche):
    try:
        sql = "delete from lanche where codigoLanche = '{}'".format(codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletada!")
    except Exception as erro:
        print(erro)