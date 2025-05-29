# Gerenciamento de tarefas: Criar, visualizar e atualizar listas de tarefas ou projetos.	
# Módulo: Principal / Main
# 29/05/2025
# Autor: Paulo Vilela, Kauan Ferreira, Franscisco Carlos e Vinícius Henrique

# Biblioteca
import os
import tarefas_criar
import tarefas_visualizar
import tarefas_atualizar
import tarefas_excluir

# Dicionário
tarefas = {} #chave: identificador (id) -> pacientes{"id" = id, "nome" = nome, "celular" = celular}

# Functions
def menu():
    print('\n\n Gerenciamento de Tarefas') # Título
    print('\n\n Menu de opções: ') 
    print('\33[95m 1 - Criar \33[m')
    print('\33[94m 2 - Visualizar\33[m')
    print('\33[94m 3 - Atualizar\33[m')
    print('\33[91m 4 - Excluir\33[m')
    print(' 0 - Sair')

def options(select):
    if select == 1: tarefas_criar.criar()
    elif (select == 2): tarefas_visualizar.visualizar()
    elif (select == 3): tarefas_atualizar.atualizar()
    elif (select == 4): tarefas_excluir.excluir()
    elif (select == 0): print('Até mais!')
    else: print('Opção inválida.')

select = None
while (select != 0):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela  

    menu() # Chama a função "menu"
    select = int(input('\033[1;92m \nEscolha uma opção: \033[m'))
    options(select) # Chama a função "options"

    input('\n \033[0;32;4m Pressione ENTER para continuar. \033[m \n')
 