def is_integer(entrada):
    """
    Verifica se a entrada é um número sem gerar exceções.

    Args:
        entrada (str): A entrada fornecida pelo usuário.

    Returns:
        bool: True se for número, False caso contrário.
    """
    entrada = entrada.strip()  # Remove espaços em branco
    if not entrada:
        return False  # Retorna False para string vazia

    # Verifica se é um número decimal ou inteiro
    if entrada.isdigit():  # Verifica inteiros
        return True
    elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1:
        return True  # Verifica decimais
    elif entrada[0] in ('-', '+') and (entrada[1:].isdigit() or
                                       (entrada[1:].replace('.', '', 1).isdigit() and entrada[1:].count('.') <= 1)):
        return True  # Verifica números com sinal (+ ou -)

    return False



def funcao_cadastrar_contato(id): # Meu id: 4975534 - Caio Fellipe Bezerra Cabral - Estudante - 85997521399
    print('\033[1;34m=' * 20 + ' MENU CADASTRAR CONTATO ' + '=' * 20 + '\033[m')
    while True:
        id = input('Id do Contato: ')
        if is_integer(id):
            id = int(id)
            break
        else:
            print('\033[1;31mOpção inválida! Tente novamente.\033[m')

    dict_contato = {}
    dict_contato['id'] = id
    dict_contato['nome'] = input('Por favor, entre com o nome do contato: ')
    dict_contato['atividade'] = input('Por favor, entre com a atividade do contato: ')
    dict_contato['telefone'] = int(input('Por favor, entre com o telefone do contato: '))
    lista_contatos.append(dict_contato.copy())
    print()

def funcao_consultar_contatos():
    while True:
        print('\033[1;34m=' * 20 + ' MENU CONSULTAR CONTATOS ' + '=' * 20 + '\033[m')
        print('Escolha a opção desejada:')
        print('1 - Consultar todos os Contatos')
        print('2 - Consultar Contato por id')
        print('3 - Consultar Contato(s) por Atividade')
        print('4 - Retornar ao Menu Principal')
        escolha = int(input(''))
        print()
        if escolha == 1:
            print('\033[34mLista de Contatos:\033[m') # Frase destacada a azul para facilitar a visualização.
            for contato in lista_contatos:
                print(f'ID: {contato["id"]}') # Modo mais organizado de exibir os contatos.
                print(f'Nome: {contato["nome"]}')
                print(f'Atividade: {contato["atividade"]}')
                print(f'Telefone: {contato["telefone"]}')
                print() # Linha em branco para facilitar a visualização.

        elif escolha == 2:
            id_consulta = int(input('\033[34mDigite o id do contato: \033[m'))
            encontrado = 0
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print(f'ID: {contato["id"]}')
                    print(f'Nome: {contato["nome"]}')
                    print(f'Atividade: {contato["atividade"]}')
                    print(f'Telefone: {contato["telefone"]}')
                    print()
                    encontrado += 1
                    break

            if encontrado == 0: # Através dessa condição, só irá fazer o print da mensagem abaixo se, de fato, o ID não foi encontrado.
                print('\033[1;31mId inválido! Tente novamente.\033[m')

        elif escolha == 3:
            atividade_consulta = input('\033[34mDigite a atividade do(s) Contato(s): \033[m')
            encontrado = 0
            for contato in lista_contatos:
                if contato['atividade'] == atividade_consulta:
                    print(f'ID: {contato["id"]}')
                    print(f'Nome: {contato["nome"]}')
                    print(f'Telefone: {contato["telefone"]}')
                    print(f'Atividade: {contato["atividade"]}')
                    print()
                    encontrado += 1

            if encontrado == 0:
                print('\033[1;31mAtividade inválida! Tente novamente.\033[m')

        elif escolha == 4:
            return # Sai da função e retorna ao programa principal, sem precisar acionar o break.

        else: print('\033[1;31mOpção inválida! Tente novamente.\033[m')

def funcao_remover_contato():
    print('\033[1;34m=' * 21 + ' MENU REMOVER CONTATO ' + '=' * 21 + '\033[m')
    while True:
        id_remocao = int(input('\033[34mDigite o ID do contato para a remoção: \033[m'))
        encontrado = 0
        for contato in lista_contatos: # Loop para passar por todos os contatos da lista e verificar se o id digitado corresponde ao id de algum deles.
            if contato['id'] == id_remocao:
                lista_contatos.remove(contato)
                print(f'\033[34mContato com o ID {id_remocao} foi removido com sucesso!\033[m')
                encontrado += 1
                return

        if encontrado == 0:
            print('\033[1;31mId inválido! Tente novamente.\033[m')


def main():
# Programa Principal

    print('=' * 10 + ' Sistema desenvolvido por Caio Fellipe Bezerra Cabral ' + '=' * 10)
    print('\033[7;36m=-' * 10 + ' Contatos - Caio Cabral ' + '-=' * 10 + '\033[m')
    global lista_contatos
    lista_contatos = []  # Definição da lista antes do loop, para não ocorrer de ela ser esvaziada a cada repetição.

    while True:
        print('\033[1;36m=' * 24 + ' MENU PRINCIPAL ' + '=' * 24 + '\033[m')
        print('Escolha a opção desejada:')
        print('1 - Cadastrar Contato')
        print('2 - Consultar Contato')
        print('3 - Remover Contato')
        print('4 - Sair')
        var_escolha = input('')  # Campo de entrada pelo teclado, em que se define a opção escolhida.
        var_id_global = 0
        if var_escolha == '1':
            funcao_cadastrar_contato(var_id_global)
        elif var_escolha == '2':
            funcao_consultar_contatos()
        elif var_escolha == '3':
            funcao_remover_contato()
        elif var_escolha == '4':
            break
        else:
            print('\033[1;31mOpção inválida! Tente novamente.\033[m')

    # Saída final com o print da lista de contatos atualizada:

    print('\033[1;36m=' * 17 + ' LISTA DE CONTATOS ATUALIZADA ' + '=' * 17 + '\033[m')
    for contato in lista_contatos:
        print(f'ID: {contato["id"]}')
        print(f'Nome: {contato["nome"]}')
        print(f'Telefone: {contato["telefone"]}')
        print(f'Atividade: {contato["atividade"]}')


# Verifica se este arquivo é o principal sendo executado
if __name__ == "__main__":
    print('Com quem eu falo?')
    prompt = input('')
    print(f'Ola {prompt}!!! Disse a voce que eu comeco aqui...')
    main()








