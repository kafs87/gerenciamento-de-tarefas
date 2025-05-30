# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.	
# Módulo: Principal / Main
# 29/05/2025
# Autor: Paulo Vilela, Kauan Ferreira, Franscisco Carlos e Vinícius Henrique

# Bibliotecas
import os
from dicionario import tarefas, proximo_id
import tarefas_criar
import tarefas_visualizar
import tarefas_atualizar
import tarefas_excluir

# Functions
def menu():
    print('\n\n Gerenciamento de Tarefas') # Título
    print('\n\n Menu de opções: ') 
    print('\33[95m 1 - Criar \33[m')
    print('\33[94m 2 - Visualização Simples\33[m')
    print('\33[94m 3 - Visualização Avançada\33[m')
    print('\33[94m 4 - Atualizar\33[m')
    print('\33[91m 5 - Excluir\33[m')
    print(' 0 - Sair')

def options(select):
    if select == 1: tarefas_criar.criar()
    elif (select == 2): tarefas_visualizar.visualizacao_simples()
    elif (select == 3): tarefas_visualizar.visualizacao_avancada()
    elif (select == 4): tarefas_atualizar.atualizar()
    elif (select == 5): tarefas_excluir.excluir()
    elif (select == 0): print('Até mais!')
    else: print('Opção inválida.')

select = None
while select != 0:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
    menu() #Exibe o menu
    try:
        select = int(input('\033[1;92m \nEscolha uma opção: \033[m'))
        options(select)
    except ValueError:
        print('Por favor, digite um número válido.')

    input('\n \033[0;32;4m Pressione ENTER para continuar. \033[m \n')
 