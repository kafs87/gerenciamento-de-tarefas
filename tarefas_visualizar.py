# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.
# Módulo: Visualização
# 29/05/2025
# Autor: Kauan Ferreira da Silva

# Bibliotecas
from dicionario import tarefas, proximo_id

def visualizacao_simples():
    print('\n--- Visualização Simples de Tarefas ---\n')
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    print(f'{"ID":<4} | {"Título":<15} | {"Descrição":<20} | {"Status":<12} | {"Data":<10} | {"Prioridade":<10} | {"Responsável":<15}')
    print('-' * 100)
    for id in tarefas:
        print(tarefas[id].get('id'), "-", tarefas[id].get('titulo'), "-", tarefas[id].get('descricao'), "-", tarefas[id].get('status'), "-", tarefas[id].get('data'), "-", tarefas[id].get('prioridade'), "-", tarefas[id].get('responsavel'))

def visualizacao_avancada():
    print('\n--- Visualização Avançada de Tarefas ---\n')
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return

    # Filtro opcional ao usuário
    while True:
        aplicar_filtro = input('Deseja aplicar um filtro? (s/n): ').strip().lower()
        filtro_campo = None
        filtro_valor = None
        while aplicar_filtro not in ['nao', 'n', 'não', 's', 'sim']:
            aplicar_filtro = input('Resposta inválida. Deseja aplicar um filtro? (s/n): ')
        break

    if aplicar_filtro in ['s', 'sim']:
        print('\nFiltrar por:')
        print('| 1 - ID | 2 - Título | 3 - Descrição | 4 - Status | 5 - Data | 6 - Prioridade | 7 - Responsável |')
        try:
            campo = int(input('Escolha o campo para filtrar (ex: 4): '))
            valor = input('Digite o valor para o filtro (ex: Pendente): ').strip()
            campos = {
                1: 'id', 2: 'titulo', 3: 'descricao',
                4: 'status', 5: 'data', 6: 'prioridade', 7: 'responsavel'
            }
            if campo not in campos:
                print('Campo inválido.')
                return
            filtro_campo = campos[campo]
            filtro_valor = valor
        except ValueError:
            print('Entrada inválida.')
            return
        
    if aplicar_filtro in ['n', 'nao', 'não', 's', 'sim']:    
    # Pergunta ao usuário quais campos quer visualizar
        print('\n| 1 - ID | 2 - Título | 3 - Descrição | 4 - Status | 5 - Data | 6 - Prioridade | 7 - Responsável |')
        entrada = input('Quais campos você quer visualizar? (ex: 2, 3, 6): ').strip()
        try:
            escolhas = [int(i.strip()) for i in entrada.split(',')]
        except ValueError:
            print('Entrada inválida.')
            return

        campos = {
            1: 'id', 2: 'titulo', 3: 'descricao',
            4: 'status', 5: 'data', 6: 'prioridade', 7: 'responsavel'
        }

        print('\n--- Tarefas ---')
        for tarefa in tarefas.values():
            # Aplicar filtro se selecionado
            if filtro_campo and str(tarefa[filtro_campo]).lower() != filtro_valor.lower():
                continue

            for i in escolhas:
                if i in campos:
                    print(f"{campos[i].capitalize()}: {tarefa[campos[i]]}")
            print('---------------')