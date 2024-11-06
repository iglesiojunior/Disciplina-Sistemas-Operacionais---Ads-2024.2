import psutil
import os

def enter_to_continue():
    input("Pressione enter para continuar")


def show_menu():
    menu = """
    ==========================================
    1 - Exibir todas os processos disponíveis
    2 - "matar" processos
    
    0 - Sair do programa
    ==========================================
    """
    print(menu)

def main():
    estado_loop = -1
    while(estado_loop != 0):
        show_menu()
        estado_loop = int(input(">>>>"))
        if(estado_loop == 1):
            list = psutil.pids()
            for pid in list:
                p = psutil.Process(pid)
                print(f"{pid} - {p.name()}   Status ---> {p.status()}")
        elif(estado_loop == 2):
            print("Insira o id do processo desejado: ")
        
main()