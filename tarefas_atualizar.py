# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.
# Módulo: Atualização
# 30/05/2025
# Autor: Francisco Carlos Gimenes Neto (com melhorias para padronização)

# Bibliotecas
from dicionario import tarefas, proximo_id
from tarefas_criar import status_option, prioridade_option  # Utilizar validações já existentes
import datetime

def ajustar_texto(texto, limite):
    return (texto[:limite - 3] + '...') if len(texto) > limite else texto

def confirmar_acao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'nao', 'não']:
            return False
        else:
            print('\33[91mResposta inválida. Digite "s" para sim ou "n" para não.\33[m')

def atualizar():
    print('\33[95m\n--- Atualização de Tarefas ---\n\33[m')
    if not tarefas:
        print('\33[91mNenhuma tarefa cadastrada.\33[m')
        return

    idAtt = None
    tarefaAtt = None
    while True:
        try:
            idAtt = int(input('Qual o ID da tarefa que você quer atualizar?: '))
        except ValueError:
            print('\33[91mID inválido! Digite um número inteiro.\33[m')
            continue

        for tarefa in tarefas:
            if tarefas[tarefa]['id'] == idAtt:
                tarefaAtt = tarefas[tarefa]
                break
        if tarefaAtt:
            break
        else:
            print('\33[91mDigite um ID de uma tarefa existente.\33[m')

    print('\nTAREFA ATUAL:')
    print(f'{"ID":<4} | {"Título":<15} | {"Descrição":<40} | {"Status":<12} | {"Data":<10} | {"Prioridade":<10} | {"Responsável":<15}')
    print('-' * 125)
    print(f'{ajustar_texto(str(tarefaAtt["id"]), 4):<4} | '
        f'{ajustar_texto(tarefaAtt["titulo"], 15):<15} | '
        f'{ajustar_texto(tarefaAtt["descricao"], 40):<40} | '
        f'{ajustar_texto(tarefaAtt["status"], 12):<12} | '
        f'{ajustar_texto(tarefaAtt["data"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["prioridade"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["responsavel"], 15):<15}')

    if confirmar_acao('\nQuer atualizar o título da tarefa? (s/n): '):
        novo_titulo = input('Digite o título da tarefa: ')
        if not novo_titulo.strip():
            print('\33[91mTítulo não pode ser vazio! Mantendo o título anterior.\33[m')
        else:
            tarefaAtt["titulo"] = novo_titulo

    if confirmar_acao('Quer atualizar a descrição da tarefa? (s/n): '):
        nova_desc = input('Digite a descrição da tarefa: ')
        if not nova_desc.strip():
            print('\33[91mDescrição não pode ser vazia! Mantendo a anterior.\33[m')
        else:
            tarefaAtt["descricao"] = nova_desc

    if confirmar_acao('Quer atualizar o status da tarefa? (s/n): '):
        status = input('Digite o status da tarefa ([1]Pendente [2]Em Andamento [3]Concluída): ')
        tarefaAtt["status"] = status_option(status)

    if confirmar_acao('Quer atualizar a data da tarefa? (s/n): '):
        nova_data = input('Digite a data de conclusão (DD/MM/AAAA): ')
        try:
            dia, mes, ano = map(int, nova_data.split('/'))
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0):
                raise ValueError
            tarefaAtt["data"] = nova_data
        except ValueError:
            print('\33[91mData inválida! Mantendo a data anterior.\33[m')

    if confirmar_acao('Quer atualizar a prioridade da tarefa? (s/n): '):
        prioridade = input('Digite a prioridade da tarefa ([1]Baixa [2]Média [3]Alta): ')
        tarefaAtt["prioridade"] = prioridade_option(prioridade)

    if confirmar_acao('Quer atualizar o responsável da tarefa? (s/n): '):
        novo_resp = input('Digite o responsável pela tarefa: ')
        if not novo_resp.strip():
            print('\33[91mResponsável não pode ser vazio! Mantendo o anterior.\33[m')
        else:
            tarefaAtt["responsavel"] = novo_resp

    print('\n\33[94mTAREFA ATUALIZADA (pré-confirmação):\33[m')
    print(f'{"ID":<4} | {"Título":<15} | {"Descrição":<40} | {"Status":<12} | {"Data":<10} | {"Prioridade":<10} | {"Responsável":<15}')
    print('-' * 125)
    print(f'{ajustar_texto(str(tarefaAtt["id"]), 4):<4} | '
        f'{ajustar_texto(tarefaAtt["titulo"], 15):<15} | '
        f'{ajustar_texto(tarefaAtt["descricao"], 40):<40} | '
        f'{ajustar_texto(tarefaAtt["status"], 12):<12} | '
        f'{ajustar_texto(tarefaAtt["data"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["prioridade"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["responsavel"], 15):<15}')

    if confirmar_acao('\nDeseja mesmo atualizar a tarefa? (s/n): '):
        print('\nAtualizando...')
        for tarefa in tarefas:
            if tarefas[tarefa]['id'] == idAtt:
                tarefas[tarefa] = tarefaAtt
                break
        print('\33[92m\nTarefa Atualizada com Sucesso!\33[m')
    else:
        print('\33[91mOperação Cancelada!\33[m')

