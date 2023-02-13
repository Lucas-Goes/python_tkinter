import tkinter as tk
from tkinter import ttk

# Cria a janela principal
janela = tk.Tk()
janela.title("Acompanhamento de Log")

# Define o tamanho da janela
janela.geometry("800x600")

# Cria um frame para colocar os botões e entradas de texto
frame_botoes = tk.Frame(janela, bg="grey", height=50)
frame_botoes.pack(fill="x")

# Adiciona um botão Iniciar
botao_iniciar = tk.Button(frame_botoes, text="Iniciar", width=10)
botao_iniciar.pack(side="left", padx=10)

# Adiciona uma entrada de texto Nome
entrada_nome = tk.Entry(frame_botoes)
entrada_nome.pack(side="left", padx=10)

# Adiciona um combobox Tipo
valores = ["Tipo 1", "Tipo 2", "Tipo 3"]
combobox_tipo = ttk.Combobox(frame_botoes, values=valores, state="readonly")
combobox_tipo.pack(side="left", padx=10)

# Cria um frame para colocar a tabela
frame_tabela = tk.Frame(janela, bg="grey", height=500)
frame_tabela.pack(fill="x", pady=10)

# Adiciona uma tabela com 5 colunas
tabela = ttk.Treeview(frame_tabela, columns=("Nome", "Data Início", "Data Fim", "Tempo Total", "Status Final"))
tabela.pack()

# Configura as colunas da tabela
tabela.heading("#0", text="Nome", anchor="w")
tabela.heading("#1", text="Data Início", anchor="w")
tabela.heading("#2", text="Data Fim", anchor="w")
tabela.heading("#3", text="Tempo Total", anchor="w")
tabela.heading("#4", text="Status Final", anchor="w")

# Adiciona algumas linhas como exemplo
tabela.insert("", "end", text="Processo 1", values=("10/02/2023", "11/02/2023", "1 dia", "Concluído"))
tabela.insert("", "end", text="Processo 2", values=("11/02/2023", "12/02/2023", "1 dia", "Concluído"))
tabela.insert("", "end", text="Processo 3", values=("12/02/2023", "14/02/2023", "2 dias", "Em andamento"))

# Inicia a janela
janela.mainloop()
