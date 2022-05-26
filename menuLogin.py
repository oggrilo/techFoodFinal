import operacoes
import this
import conexao
this.opcao = -1


def menu():
    print('\n\nEscolha uma das opções abaixo: \n\n' +
            '1. Cadastrar Cliente\n' +
            '2. Login Cliente\n' +
            '3. Login Adiministrador\n' +
            '0. Sair')
    this.opcao = int(input())

def escolhas():
    while(this.opcao !=0 ):
        menu()
        if this.opcao == 1:
            # Coletando a digitação do usuário
            print('Digite seu nome: ')
            nomeCliente = input()
            print('Digite seu cpf: ')
            cpfCliente = input()
            print('Digite seu celular: ')
            celularCliente = input()
            print('Digite sua senha: ')
            senhaCliente = input()
            # utilizar o método cadastrar
            operacoes.inserirCliente(nomeCliente, cpfCliente, celularCliente, senhaCliente)
        elif this.opcao == 2:
            print("Digite seu CPF: ")
            cpfCliente= input()
            print("Digite sua senha: ")
            senhaCliente = input()
            operacoes.loginCliente(cpfCliente, senhaCliente)
        elif this.opcao == 3:
            print("Digite seu CPF: ")
            cpfFunc = input()
            print("Digite sua senha: ")
            senhaFunc = input()
            operacoes.loginFunc(cpfFunc, senhaFunc)
        else:
             print("Obrigado e até a proxima!")



