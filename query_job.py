import tkinter
from tkinter import ttk
from tkinter import messagebox, BOTH, END, LEFT, ttk
import customtkinter
import time
import io
import os
import sv_ttk
import csv


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

global lista
lista = ['Teste']

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # This is where the magic happens
        sv_ttk.set_theme("dark")

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{500}x{480}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="TESTE TESTE", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # create tabview
        self.options_window = customtkinter.CTkButton(self.sidebar_frame, text="Query Job",command=self.create_toplevel)
        self.options_window.grid(row=2, column=0, padx=20, pady=(10, 10))
        
        self.options_window = customtkinter.CTkButton(self.sidebar_frame, text="Histórico",command=self.create_hist_toplevel)
        self.options_window.grid(row=3, column=0, padx=20, pady=(10, 10))
        
        #atualiza valores e cria o combobox do query job
        caminho = os.path.join(os.getcwd(), 'query_jobs')
        arquivos = os.listdir(caminho)
        self.combobox_1 = customtkinter.CTkComboBox(self.sidebar_frame, values=[os.path.splitext(f)[0] for f in arquivos])
        self.combobox_1.grid(row=4, column=0, padx=20, pady=(10, 10))
        
        
    def create_hist_toplevel(self):
    
        def att_treeview():
            for i in tree.get_children():
                tree.delete(i)
            for row in csv.reader(open(filename)):
                tree.insert("", 0, values=tuple(row))
        
        #cria janela do query job
        window_hist = customtkinter.CTkToplevel(self)
        window_hist.resizable(False, False)
        window_hist.geometry("1010x390")        
        # configure grid layout (4x4)
        window_hist.grid_columnconfigure(0, weight=1)
        window_hist.grid_columnconfigure((0, 0), weight=0)
        window_hist.grid_rowconfigure((4, 4, 4), weight=1)
        
        self.eval(f'tk::PlaceWindow {str(window_hist)} center')
        window_hist.attributes('-topmost', 'true')
        
        # Cria a Treeview
        tree = ttk.Treeview(window_hist, height=10)
        tree.grid(row=0, column=0)
        
        att_tree = customtkinter.CTkButton(window_hist, text="Atualizar",command= att_treeview)
        att_tree.grid(row=1, column=0, pady=(10, 10) )
        
        # Cria a barra de rolagem vertical
        vsb = ttk.Scrollbar(window_hist, orient="vertical", command=tree.yview)
        vsb.grid(row=0, column=1, sticky="ns")

        # Configura a Treeview para usar a barra de rolagem
        tree.configure(yscrollcommand=vsb.set)

        #  ["ID_PROCESSO", "NOME_PROCESS", "DATA_INICIO", "DATA_FIM", "TEMPO_TOTAL", "STATUS"]
        # Adiciona algumas colunas e linhas de exemplo
        tree["columns"] = ("col1", "col2", "col3","col4", "col5", "col6", "col7")
        tree.column("col1", width=110, anchor="center")
        tree.column("col2", width=250, anchor="center")
        tree.column("col3", width=150, anchor="center")
        tree.column("col4", width=150, anchor="center")
        tree.column("col5", width=115, anchor="center")
        tree.column("col6", width=100, anchor="center")
        tree.column("col7", width=100, anchor="center")

        #tree.heading("#0", text="Nome", anchor="center")
        tree.column("#0", width=0,stretch = "no")
        tree.heading("col1", text="Id Processo", anchor="center")
        tree.heading("col2", text="Processo", anchor="center")
        tree.heading("col3", text="Data Inicio", anchor="center")
        tree.heading("col4", text="Data Fim", anchor="center")
        tree.heading("col5", text="Tempo Total", anchor="center")
        tree.heading("col6", text="Status", anchor="center")
        tree.heading("col7", text="Origem", anchor="center")
        
        tree.configure(height=15)
        
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 10)) # Modify the font of the body
        style.configure("Treeview.Heading", font=(None, 10))
        
        # Adicionar dados ao arquivo de log
        filename = "log.csv"

        # Atualizar interface gráfica
        for row in csv.reader(open(filename)):
            tree.insert("", 0, values=tuple(row))

    def create_toplevel(self):
            
        # Center the window, and set minsize
        def update_label2():
            self.update()
            self.minsize(self.winfo_width(), self.winfo_height())
            x_cordinate = int((self.winfo_screenwidth()/2) - (self.winfo_width()/2))
            y_cordinate = int((self.winfo_screenheight()/2) - (self.winfo_height()/2))
            window.geometry("+{}+{}".format(x_cordinate, y_cordinate))
        
        def on_close():
            self.options_window.configure(state="normal")
            window.destroy()
            #self.state("normal")

        def atualizar_combo():
            caminho = os.path.join(os.getcwd(), 'query_jobs')
            arquivos = os.listdir(caminho)
            self.combobox_1.configure(values=[os.path.splitext(f)[0] for f in arquivos])
            self.combobox_1.set("")
            
        def salva_query_job():
            nome_arq_original = window.job_query_name.get(1.0, "end-1c")
            nome_arquivo_formatado = (nome_arq_original.split(".")[0]).strip() #remove tudo após algum ponto e espaços em branco no inicio ou final
            caminho = os.path.join(os.getcwd(), 'query_jobs')
            if nome_arquivo_formatado != "Nome Query Job":
                try:
                    with open(os.path.join(caminho, nome_arquivo_formatado+".txt"), 'w') as arquivo: # abre o arquivo para escrita
                        texto = window.sql_code.get("1.0", END) # obtém o texto do campo de texto
                        texto_check = window.sql_code.get(1.0, "end-1c")
                        if texto_check != "Código SQL...":
                            arquivo.write(texto) # escreve o texto no arquivo
                            arquivo.close() # fecha o arquivo
                            atualizar_combo()
                            window.grab_set()
                            messagebox.showinfo("Salvar arquivo", "Arquivo salvo com sucesso!")
                        else:
                            window.grab_set()
                            messagebox.showerror("Dados Incorretos", "Escreva o código SQL!") 
                except:
                    window.grab_set()
                    messagebox.showerror("Salvar arquivo", "Erro ao salvar o arquivo!")                   
            else:
                window.grab_set()
                messagebox.showerror("Dados Incorretos", "Defina um nome para o Query Job!") 
               
        #trata alguns atributos na janela pai            
        self.options_window.configure(state="disabled") #desativa botao
        #self.state("iconic") #minimiza janela pai
        
        
        #cria janela do query job
        window = customtkinter.CTkToplevel(self)
        window.resizable(False, False)
        window.geometry("950x650")        
        
        #self.eval(f'tk::PlaceWindow {str(window)} center')
        update_label2()
        window.attributes('-topmost', 'true')
        # configure grid layout (4x4)
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure((0, 0), weight=0)
        window.grid_rowconfigure((4, 4, 4), weight=1)
        #configura botao para salvar a query
        window.options_window = customtkinter.CTkButton(window, text="Salvar Query Job",command=salva_query_job)
        window.options_window.grid(row=1, column=1, padx=(0, 0), pady=(10, 30))
        window.title("Data Flow - Query Job")
        #configura o campo para o nome do query job
        window.job_query_name = customtkinter.CTkTextbox(window, width=300, height=35)
        window.job_query_name.grid(row=1, column=0, padx=(25, 20), pady=(10, 30), sticky="nsew")
        #configura o campo onde sera escrita a query 
        window.sql_code = customtkinter.CTkTextbox(window, width=900, height=520)     
        window.sql_code.grid(row=3, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        window.sql_code.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        window.job_query_name.insert("0.0","Nome Query Job")
        window.sql_code.insert("0.0","Código SQL...")  

        
        window.protocol("WM_DELETE_WINDOW", on_close)
        
    # Center the window, and set minsize
    def update_label(self):
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        x_cordinate = int((self.winfo_screenwidth()/2) - (self.winfo_width()/2))
        y_cordinate = int((self.winfo_screenheight()/2) - (self.winfo_height()/2))
        self.geometry("+{}+{}".format(x_cordinate, y_cordinate))


if __name__ == "__main__":
    app = App()
    app.update_label()
    #app.eval('tk::PlaceWindow . center')
    app.mainloop()