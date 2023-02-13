import tkinter
from tkinter import messagebox, BOTH, END, LEFT, ttk
import customtkinter
import time
import io
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

global lista
lista = ['Teste']

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

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

        # create tabview
        self.options_window = customtkinter.CTkButton(self.sidebar_frame, text="Query Job",command=self.create_toplevel)
        self.options_window.grid(row=2, column=0, padx=20, pady=(10, 10))
        
        #atualiza valores e cria o combobox do query job
        caminho = os.path.join(os.getcwd(), 'query_jobs')
        arquivos = os.listdir(caminho)
        self.combobox_1 = customtkinter.CTkComboBox(self.sidebar_frame, values=[os.path.splitext(f)[0] for f in arquivos])
        self.combobox_1.grid(row=4, column=0, padx=20, pady=(10, 10))
        
        

    def create_toplevel(self):
            
        def on_close():
            self.options_window.configure(state="normal")
            window.destroy()
            self.state("normal")

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
        self.state("iconic") #minimiza janela pai
        
        
        #cria janela do query job
        window = customtkinter.CTkToplevel(self)
        window.resizable(False, False)
        window.geometry("950x650")        
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


if __name__ == "__main__":
    app = App()
    app.mainloop()