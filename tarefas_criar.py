# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.
# Módulo: Criação
# 29/05/2025
# Autor: Paulo Augusto de Jesus Vilela

# Bibliotecas
import datetime
# Importando o dicionário de tarefas e o próximo ID
from dicionario import tarefas, proximo_id

# Função para verificar e retornar o status da tarefa
def status_option(status):
    opcoes = {
        '1': 'Pendente',
        '2': 'Em Andamento',
        '3': 'Concluída'
    }
    if status in opcoes:
        return opcoes[status]
    else:
        print('\33[91mOpção inválida! Usando "Pendente" como padrão.\33[m')
        return 'Pendente'

# Função para verificar e retornar a prioridade da tarefa
def prioridade_option(prioridade):
    opcoes = {
        '1': 'Baixa',
        '2': 'Média',
        '3': 'Alta'
    }
    if prioridade in opcoes:
        return opcoes[prioridade]
    else:
        print('\33[91mOpção inválida! Usando "Baixa" como padrão.\33[m')
        return 'Baixa'
    
# Função para criar uma nova tarefa
def criar():
    # Variável global para o próximo ID
    global proximo_id

    #cabeçalho
    print('\33[95m\n--- Criação de Tarefas ---\n\33[m')\
    
    titulo = input('Digite o título da tarefa: ')
    # Verifica se o título não está vazio
    if not titulo.strip():
        print('\33[91mTítulo não pode ser vazio! Usando "Tarefa sem título" como padrão.\33[m')
        titulo = 'Tarefa sem título'

    descricao = input('Digite a descrição da tarefa: ')
    # Verifica se a descrição não está vazia
    if not descricao.strip():
        print('\33[91mDescrição não pode ser vazia! Usando "Sem descrição" como padrão.\33[m')
        descricao = 'Sem descrição'

    status = input('Digite o status da tarefa ([1]Pendente [2]Em Andamento [3]Concluída): ')
    #verifica se o status é válido
    status = status_option(status)
        
    data = input('Digite a data de conclusão (DD/MM/AAAA): ')
    # Verifica se a data está no formato correto
    try:
        dia, mes, ano = map(int, data.split('/'))
        if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0):
            raise ValueError
    except ValueError:
        print('\33[91mData inválida! Usando a data atual como padrão.\33[m')
        data = datetime.datetime.now().strftime("%d/%m/%Y")  # Data atual no formato DD/MM/AAAA

    prioridade = input('Digite a prioridade da tarefa ([1]Baixa [2]Média [3]Alta): ')
    # Verifica se a prioridade é válida
    prioridade = prioridade_option(prioridade)
    
    responsavel = input('Digite o responsável pela tarefa: ')
    # Verifica se o responsável não está vazio

    
    if not responsavel.strip():
        print('\33[91mResponsável não pode ser vazio! Usando "Sem responsável" como padrão.\33[m')
        responsavel = 'Sem responsável'
    
    print(f'\33[95m--- Tarefa Criada com Sucesso! ---\n id: {proximo_id}\33[m')

    

    # Armazenar a tarefa no dicionário
    tarefas[proximo_id[0]] = {
        'id': proximo_id[0],
        'titulo': titulo,
        'descricao': descricao,
        'status': status,
        'data': data,

        'prioridade': prioridade,
        'responsavel': responsavel
    }
    proximo_id[0] += 1
