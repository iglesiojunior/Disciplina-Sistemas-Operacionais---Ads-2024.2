import threading
from datetime import datetime
import pytz
import time
import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_horario(cidade, fuso_horario):
    while True:
        timezone = pytz.timezone(fuso_horario)
        horario = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Horário em {cidade}: {horario}")
        time.sleep(5)  
        limpar_console()


fusos = {
    "Brasil (Brasília)": "America/Sao_Paulo",
    "Washington, D.C.": "America/New_York",
    "Londres": "Europe/London",
    "Japão (Tóquio)": "Asia/Tokyo"
}


threads = []
for cidade, fuso_horario in fusos.items():
    thread = threading.Thread(target=mostrar_horario, args=(cidade, fuso_horario))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
