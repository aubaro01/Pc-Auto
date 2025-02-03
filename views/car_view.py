import customtkinter as ctk
from tkinter import ttk



#Tirar dados de exemplo.
#Melhorar interface, trabalhar mais no update. Criar novas relações entre os carros e os clientes

class CarView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Veículos")
        self.geometry("1000x700")
        self.resizable(True, True)

     
        self.configure(bg="#2e2e2e")

        self.label_title = ctk.CTkLabel(self, text="Gerenciamento de Veículos", font=("Arial", 26, "bold"), fg_color="#1f6aa5", text_color="white")
        self.label_title.pack(fill="x", pady=(0, 20))

        # Barra de Pesquisa
        self.search_frame = ctk.CTkFrame(self, fg_color="#2e2e2e")
        self.search_frame.pack(pady=10, padx=20, fill="x")

        self.search_label = ctk.CTkLabel(self.search_frame, text="Pesquisar:", font=("Arial", 14), fg_color="#2e2e2e", text_color="white")
        self.search_label.grid(row=0, column=0, padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self.search_frame, width=200, fg_color="#1f6aa5", text_color="white", border_color="#1f6aa5", border_width=2)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = ctk.CTkButton(self.search_frame, text="Buscar", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.pesquisar_veiculos)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        # Tabela
        self.frame_table = ctk.CTkFrame(self, fg_color="#2e2e2e")
        self.frame_table.pack(pady=10, padx=20, fill="both", expand=True)

        # Estilo da Tabela
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Arial", 12), rowheight=40, background="#2e2e2e", fieldbackground="#2e2e2e", foreground="white", bordercolor="#1f6aa5")
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#1f6aa5", foreground="white", bordercolor="#1f6aa5")
        style.map("Treeview", background=[("selected", "#1f6aa5")])

        self.table = ttk.Treeview(self.frame_table, columns=("Marca", "Modelo", "Cliente", "Matricula", "Km", "OBS", "Ações"), show="headings")
        self.table.heading("Marca", text="Marca")
        self.table.heading("Modelo", text="Modelo")
        self.table.heading("Cliente", text="Cliente")
        self.table.heading("Matricula", text="Matricula")
        self.table.heading("Km", text="Km")
        self.table.heading("OBS", text="Observações")
        self.table.heading("Ações", text="Ações")
        self.table.pack(side="left", fill="both", expand=True)

        # Barra de Scroll
        scrollbar = ttk.Scrollbar(self.frame_table, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.ver_veiculos()

    def ver_veiculos(self):
        # Dados de exemplo
        veiculos = [
            {"Marca": "Toyota", "Modelo": "Corolla", "Cliente": "João Silva", "Matricula": "ABC-1234", "Km": 50000, "OBS": "Revisão em dia"},
            {"Marca": "Honda", "Modelo": "Civic", "Cliente": "Maria Oliveira", "Matricula": "XYZ-5678", "Km": 30000, "OBS": "Troca de óleo recente"},
            {"Marca": "Ford", "Modelo": "Focus", "Cliente": "Carlos Souza", "Matricula": "DEF-9012", "Km": 45000, "OBS": "Pneus novos"}
        ]
        for row in self.table.get_children():
            self.table.delete(row)
        for veiculo in veiculos:
            self.table.insert("", "end", values=(veiculo["Marca"], veiculo["Modelo"], veiculo["Cliente"], veiculo["Matricula"], veiculo["Km"], veiculo["OBS"], "Ações"))

        # Adicionar botões de ação na tabela
        for idx, veiculo in enumerate(veiculos):
            self.table.insert("", "end", values=(veiculo["Marca"], veiculo["Modelo"], veiculo["Cliente"], veiculo["Matricula"], veiculo["Km"], veiculo["OBS"]))
            self.table.set(self.table.get_children()[idx], column="Ações", value=self.criar_botoes_acoes())

    def criar_botoes_acoes(self):
        frame = ctk.CTkFrame(self.table, fg_color="#2e2e2e")
        add_button = ctk.CTkButton(frame, text="Adicionar", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.adicionar_veiculo)
        add_button.pack(side="left", padx=5)
        edit_button = ctk.CTkButton(frame, text="Editar", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.editar_veiculo)
        edit_button.pack(side="left", padx=5)
        delete_button = ctk.CTkButton(frame, text="Remover", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.remover_veiculo)
        delete_button.pack(side="left", padx=5)
        return frame

    def pesquisar_veiculos(self):
        termo_pesquisa = self.search_entry.get().lower()
        veiculos = [
            {"Marca": "Toyota", "Modelo": "Corolla", "Cliente": "João Silva", "Matricula": "ABC-1234", "Km": 50000, "OBS": "Revisão em dia"},
            {"Marca": "Honda", "Modelo": "Civic", "Cliente": "Maria Oliveira", "Matricula": "XYZ-5678", "Km": 30000, "OBS": "Troca de óleo recente"},
            {"Marca": "Ford", "Modelo": "Focus", "Cliente": "Carlos Souza", "Matricula": "DEF-9012", "Km": 45000, "OBS": "Pneus novos"}
        ]
        resultados = [veiculo for veiculo in veiculos if termo_pesquisa in veiculo["Matricula"].lower() or termo_pesquisa in veiculo["Cliente"].lower()]
        for row in self.table.get_children():
            self.table.delete(row)
        for veiculo in resultados:
            self.table.insert("", "end", values=(veiculo["Marca"], veiculo["Modelo"], veiculo["Cliente"], veiculo["Matricula"], veiculo["Km"], veiculo["OBS"], "Ações"))

        # Adicionar botões de ação na tabela
        for idx, veiculo in enumerate(resultados):
            self.table.set(self.table.get_children()[idx], column="Ações", value=self.criar_botoes_acoes())

    def adicionar_veiculo(self):
        print("Ação: Adicionar Veículo")

    def editar_veiculo(self):
        print("Ação: Editar Veículo")

    def remover_veiculo(self):
        print("Ação: Remover Veículo")

if __name__ == "__main__":
    app = CarView()
    app.mainloop()