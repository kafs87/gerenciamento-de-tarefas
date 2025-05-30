# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.
# Módulo: Visualização
# 29/05/2025
# Autor: Paulo Augusto de Jesus Vilela

tarefas = {}# chave: identificador (id) -> tarefas{"id" = id, "titulo" = titulo, "descrição" = descrição, "status" = status, "data" = data, "prioridade" = prioridade, "responsavel" = responsável}

proximo_id = 1
# Função para criar uma nova tarefa
def criar():
    global proximo_id
    print('\33[95m\n--- Criação de Tarefas ---\n\33[m')
    titulo = input('Digite o título da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    status = input('Digite o status da tarefa (Pendente/Em Andamento/Concluída): ')
    data = input('Digite a data de conclusão (DD/MM/AAAA): ')
    prioridade = input('Digite a prioridade da tarefa (Baixa/Média/Alta): ')
    responsavel = input('Digite o responsável pela tarefa: ')
    print(f'\33[95m--- Tarefa Criada com Sucesso! ---\n id: {proximo_id}\33[m')

    

    # Armazenar a tarefa no dicionário
    tarefas[proximo_id] = {
        'id': proximo_id,
        'titulo': titulo,
        'descricao': descricao,
        'status': status,
        'data': data,
        'prioridade': prioridade,
        'responsavel': responsavel
    }
    proximo_id += 1