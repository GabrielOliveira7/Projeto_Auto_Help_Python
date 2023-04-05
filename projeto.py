guinchos = ['Guincho 1 ( para veiculos simples)', 'Guincho 2 (Para veículos de porte médio)', 'Guincho 3 (Para veículos de 5 a 10 toneladas) ', 'Guincho 4 (Para veículos de 10 a 20 toneladas)']  # catálogo de guinchos disponíveis
solicitacoes = []  # lista para armazenar as solicitações de guincho

while True:  # loop infinito para o atendimento das solicitações
    # exibe o menu de opções
    print('-----Auto Help Porto-----')
    print('1 - Solicitar Suporte')
    print('2 - Verificar solicitações')
    print('3 - Cancelar solicitação')
    print('4 - Catálogo de guinchos')
    print('0 - Encerrar atendimento')

    # solicita a escolha do usuário
    escolha = input('Escolha uma opção: ')

    # verifica a escolha do usuário
    if escolha == '1':  # solicitar guincho
        # exibe o catálogo de guinchos1
        print('Catálogo de guinchos disponíveis:')
        for guincho in guinchos:
            print(guincho)

        # solicita o número do guincho desejado
        numero = input('Digite o número do guincho desejado: ')

        # verifica se o guincho está disponível
        if numero.isdigit() and int(numero) <= len(guinchos):
            guincho = guinchos[int(numero)-1]
            guinchos.remove(guincho)
            solicitacoes.append(guincho)
            print(f'Solicitação de guincho {guincho} realizada com sucesso!')
        else:
            print('Número de guincho inválido!')

    elif escolha == '2':  # verificar solicitações
        if solicitacoes:
            print('Solicitações de guincho:')
            for i, guincho in enumerate(solicitacoes):
                print(f'{i+1} - {guincho}')
        else:
            print('Não há solicitações de guincho!')

    elif escolha == '3':  # cancelar solicitação
        if solicitacoes:
            # exibe a lista de solicitações
            print('Solicitações de guincho:')
            for i, guincho in enumerate(solicitacoes):
                print(f'{i+1} - {guincho}')

            # solicita o número da solicitação a ser cancelada
            numero = input('Digite o número da solicitação a ser cancelada: ')

            # verifica se o número é válido
            if numero.isdigit() and int(numero) <= len(solicitacoes):
                guincho = solicitacoes[int(numero)-1]
                solicitacoes.remove(guincho)
                guinchos.append(guincho)
                print(f'Solicitação de guincho {guincho} cancelada com sucesso!')
            else:
                print('Número de solicitação inválido!')
        else:
            print('Não há solicitações de guincho!')

    elif escolha == '4':  # catálogo de guinchos
        print('Catálogo de guinchos disponíveis:')
        for guincho in guinchos:
            print(guincho)

    elif escolha == '0':  # encerrar atendimento
        print('Atendimento encerrado!')
        break
    