"""
Example script for testing the Forest theme

Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""

import csv
import tkinter as tk
from tkinter import ttk
import time
import threading
import logging
import tkinter.scrolledtext as ScrolledText

class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Create lists for the Comboboxes
option_menu_list = ["", "Servidor", "ProdNP", "ProdDW"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()

def log_message():
        
    logging.info("Processo Iniciado")  
    time.sleep(2)    
    for i in range(10):
        print("primeiro for ",i)
    logging.info("Extração em Andamento")   
    time.sleep(2)
    
    for i in range(10):
        print("segundo for ",i)
    logging.info("Extração Finalizada")
    time.sleep(2)
    
    for i in range(10):
        print("terceiro for ",i)
    logging.info("Carga Hadoop Finalizada")  
    
def log_message_t():
    t1 = threading.Thread(target=log_message, args=[])
    t1.start()
   

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=1, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Pane #3
pane_3 = ttk.Frame(paned)
paned.add(pane_3, weight=3)

# Create Text Log
text_log = ScrolledText.ScrolledText(pane_3, state='disabled', height = 8)
text_log.pack(expand=True, fill="both", padx=5, pady=5)
# Create textLogger
text_handler = TextHandler(text_log)

# Logging configuration
logging.basicConfig(filename='test.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s')
    
# Add the handler to logger
logger = logging.getLogger()        
logger.addHandler(text_handler)    

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_2)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=8)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Adiciona algumas colunas e linhas de exemplo
treeview["columns"] = ("col1", "col2", "col3","col4", "col5", "col6", "col7")
treeview.column("col1", width=100, anchor="center")
treeview.column("col2", width=150, anchor="center")
treeview.column("col3", width=150, anchor="center")
treeview.column("col4", width=150, anchor="center")
treeview.column("col5", width=115, anchor="center")
treeview.column("col6", width=100, anchor="center")
treeview.column("col7", width=100, anchor="center")

#tree.heading("#0", text="Nome", anchor="center")
treeview.column("#0", width=0,stretch = "no")
treeview.heading("col1", text="ID_PROCESSO", anchor="center")
treeview.heading("col2", text="NOME_PROCESSO", anchor="center")
treeview.heading("col3", text="DATA_INICIO", anchor="center")
treeview.heading("col4", text="DATA_FIM", anchor="center")
treeview.heading("col5", text="TEMPO_TOTAL", anchor="center")
treeview.heading("col6", text="STATUS", anchor="center")
treeview.heading("col7", text="ORIGEM", anchor="center")
       
# Adicionar dados ao arquivo de log
filename = "log.csv"        
#apaga os dados plotados para atualizar
for i in treeview.get_children():
    treeview.delete(i)
# Atualizar interface gráfica
for row in csv.reader(open(filename)):
    treeview.insert("", 0, values=tuple(row))

# Notebook
notebook = ttk.Notebook(pane_1)

# Tab #1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)
notebook.add(tab_1, text="Teradata")

# Button
button = ttk.Button(tab_1, text="Button", command = log_message_t)
button.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

# Radiobuttons
radio_1 = ttk.Radiobutton(tab_1, text="ProdNP", variable=d, value=1)
radio_1.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="nsew")
radio_2 = ttk.Radiobutton(tab_1, text="ProdDW", variable=d, value=2)
radio_2.grid(row=0, column=0, padx=120, pady=(0, 5), sticky="nsew")

# Entry
entry = ttk.Entry(tab_1)
entry.insert(0, "Usuario")
entry.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")
# Entry
entry = ttk.Entry(tab_1)
entry.insert(0, "Senha Teradata")
entry.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")
# Entry
entry = ttk.Entry(tab_1)
entry.insert(0, "Senha Windows")
entry.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ew")
# Entry
entry = ttk.Entry(tab_1)
entry.insert(0, "Nome da Tabela")
entry.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="ew")

# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="SQL Server")

# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="SAS")

notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Sizegrip
#sizegrip = ttk.Sizegrip(root)
#sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
#root.minsize(root.winfo_width(), root.winfo_height()) #redimensiona tamanho automaticamente
root.geometry(f"{890}x{780}") #redimensiona de acordo com os tamanhos informados
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
def main():

    t1 = threading.Thread(target=log_message, args=[])
    t1.start()

    root.mainloop()
    #t1.join()

main()
