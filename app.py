import os

restaurantes = []

def exibir_nome_do_programa():
    '''Essa funcao eh responsavel por exibir o nome do programa.'''
    print("""
      𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼
      """)

def exibir_subtitulo(texto):
    '''Essa funcao eh responsavel por exibir os subtitulos das opcoes do menu principal.'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print('')

def retornar_ao_menu_principal():
    '''Essa funcao eh responsavel por retornar ao menu principal apos a execucao de uma funcao.'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def finalizar_app():
    '''Essa funcao eh responsavel por finalizar a execucao do programa.'''
    exibir_subtitulo('Saindo do sistema...')

def menu_principal():
    '''Essa funcao eh responsavel por exibir as opcoes do menu principal.'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def menu_invalido():
    '''Essa funcao eh responsavel por exibir uma mensagem de erro quando uma opcao invalida eh escolhida.'''
    print('Opção inválida\nEscolha uma opção válida\n')
    retornar_ao_menu_principal()

def cadastrar_restaurante():
    '''Essa funcao eh responsavel por cadastrar novos restaurantes no sistema.
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes
    '''
    exibir_subtitulo('Cadastrar novo Restaurante')

    nome_restaurante = input('Nome do Restaurante: ')
    categoria = input(f'Digite a Categoria do Restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
    retornar_ao_menu_principal()

def listar_restaurantes(): 
    '''Essa funcao eh responsavel por listar todos os restaurantes cadastrados no sistema.
    
    Outputs:
    - Exibe o nome e a categoria de cada restaurante
    - Exibe o status de cada restaurante (Ativado ou Desativado)
    '''   
    if len(restaurantes) > 0:
        exibir_subtitulo('Lista de Restaurantes')
        print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status\n')

        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
        retornar_ao_menu_principal()
    else:
        exibir_subtitulo('Nenhum restaurante cadastrado')
        retornar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''Essa funcao eh responsavel por alternar o estado de um restaurante entre ativado e desativado.
    
    Inputs:
    - Nome do restaurante que deseja ativar ou desativar

    Outputs:
    - Ativa ou desativa o restaurante
    '''
    exibir_subtitulo('Alternando o estado do Restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if(nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O Restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')    

    retornar_ao_menu_principal()

def menu_escolhido():
    '''Essa funcao eh responsavel por direcionar o usuario para a funcao escolhida no menu principal.'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            menu_invalido()
    except:
        menu_invalido()

def main():
    '''Essa funcao eh responsavel por executar o programa.'''
    exibir_nome_do_programa()
    menu_principal()
    menu_escolhido()

if __name__ == '__main__':
    main()