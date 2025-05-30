# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.
# Módulo: Visualização
# 29/05/2025
# Autor: Kauan Ferreira da Silva

# Bibliotecas
from dicionario import tarefas # Importa tarefas do dicionario global

# Função que exibe todas as tarefas em formato de tabela simples
def visualizacao_simples():
    print('\n--- Visualização Simples de Tarefas ---\n')

    # Verifica se há tarefas cadastradas
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return

    # Cabeçalho da tabela com espaçamento alinhado
    print(f'{"ID":<4} | {"Título":<15} | {"Descrição":<20} | {"Status":<12} | {"Data":<10} | {"Prioridade":<10} | {"Responsável":<15}')
    print('-' * 100)

    # Itera sobre todas as tarefas e imprime os dados formatados em colunas
    for id, tarefa in tarefas.items():
        print(f'{tarefa["id"]:<4} | '
              f'{tarefa["titulo"]:<15} | '
              f'{tarefa["descricao"]:<20} | '
              f'{tarefa["status"]:<12} | '
              f'{tarefa["data"]:<10} | '
              f'{tarefa["prioridade"]:<10} | '
              f'{tarefa["responsavel"]:<15}')

# Função para visualização avançada com opção de filtro e escolha de campos
def visualizacao_avancada():
    print('\n--- Visualização Avançada de Tarefas ---\n')

    # Verifica se há tarefas cadastradas
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return

    # Inicializa as variáveis de filtro
    filtro_campo = None
    filtro_valor = None

    # Pergunta ao usuário se deseja aplicar um filtro
    while True:
        aplicar_filtro = input('Deseja aplicar um filtro? (s/n): ').strip().lower()

        # Valida a entrada
        while aplicar_filtro not in ['nao', 'n', 'não', 's', 'sim']:
            aplicar_filtro = input('Resposta inválida. Deseja aplicar um filtro? (s/n): ')
        break  # Sai do loop após resposta válida

    # Se o usuário deseja aplicar filtro
    if aplicar_filtro in ['s', 'sim']:
        print('\nFiltrar por:')
        print('| 1 - ID | 2 - Título | 3 - Descrição | 4 - Status | 5 - Data | 6 - Prioridade | 7 - Responsável |')

        try:
            # Recebe o campo e o valor que será usado para filtrar as tarefas
            campo = int(input('Escolha o campo para filtrar (ex: 4): '))
            valor = input('Digite o valor para o filtro (ex: Pendente): ').strip()

            # Mapeia os números para os nomes dos campos
            campos = {
                1: 'id', 2: 'titulo', 3: 'descricao',
                4: 'status', 5: 'data', 6: 'prioridade', 7: 'responsavel'
            }

            # Verifica se o campo informado é válido
            if campo not in campos:
                print('Campo inválido.')
                return

            # Define os critérios de filtro
            filtro_campo = campos[campo]
            filtro_valor = valor

        except ValueError:
            print('Entrada inválida.')
            return

    # Pergunta ao usuário quais campos ele quer visualizar
    print('\n| 1 - ID | 2 - Título | 3 - Descrição | 4 - Status | 5 - Data | 6 - Prioridade | 7 - Responsável |')
    entrada = input('Quais campos você quer visualizar? (ex: 2, 3, 6): ').strip()

    try:
        # Converte a entrada em uma lista de inteiros
        escolhas = [int(i.strip()) for i in entrada.split(',')]
    except ValueError:
        print('Entrada inválida.')
        return

    # Mapeamento dos números para os nomes dos campos
    campos = {
        1: 'id', 2: 'titulo', 3: 'descricao',
        4: 'status', 5: 'data', 6: 'prioridade', 7: 'responsavel'
    }

    print('\n--- Tarefas ---')

    # Percorre todas as tarefas
    for tarefa in tarefas.values():
        # Se o filtro estiver ativo e o valor do campo da tarefa for diferente, pula essa tarefa
        if filtro_campo and str(tarefa[filtro_campo]).lower() != filtro_valor.lower():
            continue

        # Para cada campo escolhido pelo usuário, imprime o valor correspondente da tarefa
        for i in escolhas:
            if i in campos:
                print(f"{campos[i].capitalize()}: {tarefa[campos[i]]}")
        print('---------------')
