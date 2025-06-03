# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.
# Módulo: Exclusão
# 29/05/2025
# Autor: Vinicius Henrique Silva Bomfim

# Bibliotecas
from dicionario import tarefas, proximo_id # Importa tarefas do dicionario global
import tarefas_visualizar

def excluir():
    print('\n--- Exclusão de Tarefas ---\n')
    tarefas_visualizar.visualizacao_simples()
    id = int(input('Identificador da Tarefa: '))

    # Consultar para excluir
    while True:
        if id in tarefas:
            resposta = input(f'Você realmente deseja excluir a tarefa {id}? (s/n)').strip().lower()

            while resposta not in ['n', 'nao', 'não', 's', 'sim']:
                resposta = input(f'Resposta inválida. Você realmente deseja excluir o paciente {id}? (s/n)')

            if resposta in ['s', 'sim']:
                del tarefas[id]
                print(f'Tarefa {id} excluído com sucesso.')
                break
            else:
                print('Tarefa não excluída.')
                break
        else: 
            print(f'Tarefa {id} não encontrada.')