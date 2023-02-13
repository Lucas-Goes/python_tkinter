import tkinter as tk
from tkinter import ttk
import csv
from tkinter import *
import pandas as pd
from datetime import datetime, timedelta

import sv_ttk



root = tk.Tk()

# This is where the magic happens
sv_ttk.set_theme("dark")

def cria_id_log():
    # Carregando o arquivo csv em um dataframe
    df = pd.read_csv("log.csv",encoding='latin-1',header=None)
    # Encontrando o valor máximo de uma coluna específica
    valor_maximo = df.iloc[:,0].max()
    # Armazenando o valor máximo em uma variável
    prox_id = valor_maximo + 1
    return prox_id

def write_log(log_id, log_data):
    #apaga os dados plotados para atualizar
    for i in tree.get_children():
        tree.delete(i)

    # Abre o arquivo CSV para escrita (cria o arquivo se ele não existir)
    with open('log.csv', 'a', newline='') as csvfile:
        # Cria o objeto escritor CSV
        writer = csv.writer(csvfile)
        # Adiciona uma nova linha com os dados do log e o ID único
        writer.writerow([log_id] + log_data)

def start_process():
    # Iniciar processamento
    inicio = datetime.now()
    
    # Adicionar dados ao arquivo de log
    filename = "log.csv"
    
    for i in range(100):
        print(i)

    final = datetime.now()
    total = (datetime.now() - inicio)
    total_formatado = str(total).split(".")[0]
    
    id_log = cria_id_log()
    # Exemplo de chamada da função para gravar um log
    write_log(id_log, ["Processo 1", inicio.strftime("%d/%m/%Y %H:%M:%S"), final.strftime("%d/%m/%Y %H:%M:%S"), total_formatado, "Concluído", "Teradata"])

    # Atualizar interface gráfica
    for row in csv.reader(open(filename)):
        tree.insert("", 0, values=tuple(row))


# Cria a Treeview
tree = ttk.Treeview(root, height=10)
tree.grid(row=0, column=0)

button = ttk.Button(root, text="Iniciar", command=start_process)
button.grid(row=1, column=0)

# Cria a barra de rolagem vertical
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.grid(row=0, column=1, sticky="ns")

# Configura a Treeview para usar a barra de rolagem
tree.configure(yscrollcommand=vsb.set)

#  ["ID_PROCESSO", "NOME_PROCESS", "DATA_INICIO", "DATA_FIM", "TEMPO_TOTAL", "STATUS"]
# Adiciona algumas colunas e linhas de exemplo
tree["columns"] = ("col1", "col2", "col3","col4", "col5", "col6", "col7")
tree.column("col1", width=100, anchor="center")
tree.column("col2", width=150, anchor="center")
tree.column("col3", width=150, anchor="center")
tree.column("col4", width=150, anchor="center")
tree.column("col5", width=115, anchor="center")
tree.column("col6", width=100, anchor="center")
tree.column("col7", width=100, anchor="center")

#tree.heading("#0", text="Nome", anchor="center")
tree.column("#0", width=0,stretch = "no")
tree.heading("col1", text="ID_PROCESSO", anchor="center")
tree.heading("col2", text="NOME_PROCESSO", anchor="center")
tree.heading("col3", text="DATA_INICIO", anchor="center")
tree.heading("col4", text="DATA_FIM", anchor="center")
tree.heading("col5", text="TEMPO_TOTAL", anchor="center")
tree.heading("col6", text="STATUS", anchor="center")
tree.heading("col7", text="ORIGEM", anchor="center")

# Adicionar dados ao arquivo de log
filename = "log.csv"

# Atualizar interface gráfica
for row in csv.reader(open(filename)):
    tree.insert("", 0, values=tuple(row))
    
tree.configure(height=20)

root.mainloop()
