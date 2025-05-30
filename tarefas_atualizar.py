# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.
# Módulo: Atualização
# 29/05/2025
# Autor: Francisco Carlos Gimenes Neto

# Bibliotecas
from dicionario import tarefas, proximo_id

def ajustar_texto(texto, limite):
    return (texto[:limite - 3] + '...') if len(texto) > limite else texto

def atualizar():
    print('\n--- Atualização de Tarefas ---\n')
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    idAtt = None
    tarefaAtt = None
    while True:
        idAtt = int(input('Qual o ID da tarefa que voce quer atualizar?: '))
        tarefaExiste = False
        for tarefa in tarefas:
            if tarefas[tarefa]['id'] == idAtt:
                tarefaExiste = True
                tarefaAtt = tarefas[tarefa]
                break
        if tarefaExiste:
            break
        else:
            print('Digite um ID de uma tarefa existente')
    print('TAREFA')
    print(f'{"ID":<4} | {"Título":<15} | {"Descrição":<20} | {"Status":<12} | {"Data":<10} | {"Prioridade":<10} | {"Responsável":<15}')
    print('-' * 100)
    print(f'{ajustar_texto(str(tarefaAtt["id"]), 4):<4} | '
        f'{ajustar_texto(tarefaAtt["titulo"], 15):<15} | '
        f'{ajustar_texto(tarefaAtt["descricao"], 20):<20} | '
        f'{ajustar_texto(tarefaAtt["status"], 12):<12} | '
        f'{ajustar_texto(tarefaAtt["data"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["prioridade"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["responsavel"], 15):<15}')

    AttTitulo = input('\nQuer atualizar o titulo da tarefa? (s/n):').strip().lower()
    if AttTitulo == 's':
        tarefaAtt["titulo"] = input('Digite o título da tarefa: ')
    AttDesc = input('Quer atualizar a descricao da tarefa? (s/n):').strip().lower()
    if AttDesc == 's':  
        tarefaAtt["descricao"] = input('Digite a descrição da tarefa: ')
    AttStatus = input('Quer atualizar o status da tarefa? (s/n):').strip().lower()
    if AttStatus == 's':
        tarefaAtt["status"] = input('Digite o status da tarefa (Pendente/Em Andamento/Concluída): ')
    AttData = input('Quer atualizar a data da tarefa? (s/n):').strip().lower()
    if AttData == 's':
        tarefaAtt["data"] = input('Digite a data de conclusão (DD/MM/AAAA): ')
    AttPrio = input('Quer atualizar a prioridade da tarefa? (s/n):').strip().lower()
    if AttPrio == 's':
        tarefaAtt["prioridade"] = input('Digite a prioridade da tarefa (Baixa/Média/Alta): ')
    AttResp = input('Quer atualizar o responsavel da tarefa? (s/n):').strip().lower()
    if AttResp == 's':
        tarefaAtt["responsavel"] = input('Digite o responsável pela tarefa: ')

    print('\nTAREFA ATUALIZADA')
    print(f'{"ID":<4} | {"Título":<15} | {"Descrição":<20} | {"Status":<12} | {"Data":<10} | {"Prioridade":<10} | {"Responsável":<15}')
    print('-' * 100)
    print(f'{ajustar_texto(str(tarefaAtt["id"]), 4):<4} | '
        f'{ajustar_texto(tarefaAtt["titulo"], 15):<15} | '
        f'{ajustar_texto(tarefaAtt["descricao"], 20):<20} | '
        f'{ajustar_texto(tarefaAtt["status"], 12):<12} | '
        f'{ajustar_texto(tarefaAtt["data"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["prioridade"], 10):<10} | '
        f'{ajustar_texto(tarefaAtt["responsavel"], 15):<15}')
    
    seleFinal = input('\nDeseja mesmo atualizar a tarefa? (s/n)').strip().lower()
    if seleFinal == 'n':
        print('Operação Cancelada!')
    elif seleFinal == 's':
        print('\nAtualizando...')
        for tarefa in tarefas:
            if tarefas[tarefa]['id'] == idAtt:
                tarefas[tarefa] = tarefaAtt
                break
        print('\nTarefa Atualizada!')
    