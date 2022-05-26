import operacoes
import this
import crudFuncionario

import menuLogin

this.opcao = -1
def menu():
    print('\n\nEscolha uma das opções abaixo: \n\n' +
            '1. Administrar Funcionário\n'                        +
            '2. Cadastrar Lanche\n'                   +
            '3. Consultar Lanche\n'                        +
            '4. Atualizar Nome do Lanche\n'                   +
            '5. Atualizar Descrição do Lanche\n'               +
            '6. Atualizar Valor do Lanche\n'               +
            '7. Atualizar Quantidade do Lanche\n'               +
            '8. Exlcuir Lanche'
            '9. Voltar\n'                          +
            '0. Sair')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            # Coletando a digitação do usuário
            crudFuncionario.operacao()
        elif this.opcao == 2:
            # Coletando a digitação do usuário
            print('Digite o Nome: ')
            nomeLanche = input()
            print('Digite a Descrição: ')
            descricaoLanche = input()
            print('Digite o Valor: ')
            valorLanche = input()
            print('Digite a Quantidade: ')
            quantidadeLanche = input()
            # utilizar o método cadastrar
            operacoes.inserir(nomeLanche, descricaoLanche, valorLanche, quantidadeLanche)
        elif this.opcao == 3:
            operacoes.selecionar()
        elif this.opcao == 4:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe o novo nome: ')
            nomeLanche = input()
            # Uso do método
            operacoes.atualizarNome(codigo, nomeLanche)
        elif this.opcao == 5:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe a nova descrição: ')
            descricaoLanche = input()
            # Uso do método
            operacoes.atualizarDescricao(codigo, descricaoLanche)
        elif this.opcao == 6:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe o novo valor: ')
            valorLanche = input()
            # Uso do método
            operacoes.atualizarValor(codigo, valorLanche)
        elif this.opcao == 7:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe a nova quantidade: ')
            quantidadeLanche = input()
            # Uso do método
            operacoes.atualizarQauntidade(codigo, quantidadeLanche)
        elif this.opcao == 8:
            print('Informe o código: ')
            codigo = input()
            operacoes.excluir(codigo)
        elif this.opcao == 9:
            menuLogin.escolhas()
        elif this.opcao == 0:
            print('Obrigado!')