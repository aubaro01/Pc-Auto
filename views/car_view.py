import customtkinter as ctk
from tkinter import ttk
from views.client_view import ClientView
from views.marcs_view import MarcsView

# Definir modo de aparência e tema padrão
ctk.set_appearance_mode("Dark")  # ou "Light"
ctk.set_default_color_theme("blue")  # "dark-blue", "green", etc.

class CarView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Veículos")
        self.geometry("1200x800")
        self.minsize(1000, 700)
        self.resizable(True, True)

        # Definir cores principais (ajuste à vontade)
        self.bg_color = "#1F2937"      # Fundo principal
        self.primary_color = "#3B82F6" # Cor primária
        self.secondary_color = "#2563EB"  # Cor secundária
        self.text_color = "#F3F4F6"    # Cor do texto

        self.configure(bg=self.bg_color)

        # Layout principal com 2 colunas: Sidebar e Área Principal
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ===== Sidebar de Navegação =====
        self.sidebar_frame = ctk.CTkFrame(self, width=220, fg_color="#2e2e2e")
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")
        self.sidebar_frame.grid_propagate(False)  # Mantém a largura fixa

        self.sidebar_title = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Menu", 
            font=("Arial", 20, "bold"),
            text_color=self.text_color
        )
        self.sidebar_title.pack(pady=20)

        self.dashboard_button = ctk.CTkButton(
            self.sidebar_frame, text="Menu", command=self.show_dashboard
        )
        self.dashboard_button.pack(pady=10, padx=20, fill="x")

        self.veiculos_button = ctk.CTkButton(
            self.sidebar_frame, text="Veículos", command=self.show_veiculos
        )
        self.veiculos_button.pack(pady=10, padx=20, fill="x")

        self.clientes_button = ctk.CTkButton(
            self.sidebar_frame, text="Clientes", command=self.show_clientes
        )
        self.clientes_button.pack(pady=10, padx=20, fill="x")

        self.relatorios_button = ctk.CTkButton(
            self.sidebar_frame, text="Relatórios", command=self.show_relatorios
        )
        self.relatorios_button.pack(pady=10, padx=20, fill="x")

        self.relatorios_button = ctk.CTkButton(
            self.sidebar_frame, text="----", command=self.show_relatorios
        )
        self.relatorios_button.pack(pady=10, padx=20, fill="x")

        # ===== Área Principal =====
        self.main_frame = ctk.CTkFrame(self, fg_color=self.bg_color)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        # Organizando: Header, Dashboard, Search e Tabela
        self.main_frame.grid_rowconfigure(3, weight=1)

        # Cabeçalho / Título
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color=self.secondary_color, corner_radius=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.label_title = ctk.CTkLabel(
            self.header_frame, 
            text="Gerenciamento de Veículos",
            font=("Arial", 24, "bold"),
            text_color=self.text_color
        )
        self.label_title.pack(pady=10)

        # Dashboard: Cards de Informações
        self.dashboard_frame = ctk.CTkFrame(self.main_frame, fg_color=self.bg_color)
        self.dashboard_frame.grid(row=1, column=0, sticky="ew", pady=10)
        self.dashboard_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Card 1: Total de Veículos
        self.card_total = ctk.CTkFrame(self.dashboard_frame, fg_color="#2D3748", corner_radius=15)
        self.card_total.grid(row=0, column=0, padx=10, sticky="nsew")
        self.total_label = ctk.CTkLabel(
            self.card_total, text="Total Veículos", font=("Arial", 16), text_color=self.text_color
        )
        self.total_label.pack(pady=(20, 5))
        self.total_value = ctk.CTkLabel(
            self.card_total, text="15", font=("Arial", 24, "bold"), text_color=self.text_color
        )
        self.total_value.pack(pady=(0, 20))

        # Card 2: Revisões Pendentes
        self.card_revisao = ctk.CTkFrame(self.dashboard_frame, fg_color="#2D3748", corner_radius=15)
        self.card_revisao.grid(row=0, column=1, padx=10, sticky="nsew")
        self.revisao_label = ctk.CTkLabel(
            self.card_revisao, text="Revisões Pendentes", font=("Arial", 16), text_color=self.text_color
        )
        self.revisao_label.pack(pady=(20, 5))
        self.revisao_value = ctk.CTkLabel(
            self.card_revisao, text="3", font=("Arial", 24, "bold"), text_color=self.text_color
        )
        self.revisao_value.pack(pady=(0, 20))

        # Card 3: Veículos Ativos
        self.card_ativos = ctk.CTkFrame(self.dashboard_frame, fg_color="#2D3748", corner_radius=15)
        self.card_ativos.grid(row=0, column=2, padx=10, sticky="nsew")
        self.ativos_label = ctk.CTkLabel(
            self.card_ativos, text="Veículos Ativos", font=("Arial", 16), text_color=self.text_color
        )
        self.ativos_label.pack(pady=(20, 5))
        self.ativos_value = ctk.CTkLabel(
            self.card_ativos, text="12", font=("Arial", 24, "bold"), text_color=self.text_color
        )
        self.ativos_value.pack(pady=(0, 20))

        # Barra de Pesquisa (abaixo do dashboard)
        self.search_frame = ctk.CTkFrame(self.main_frame, fg_color=self.bg_color)
        self.search_frame.grid(row=2, column=0, sticky="ew", pady=10, padx=10)
        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            width=250,
            placeholder_text="Pesquisar por matrícula ou cliente...",
            fg_color="#2D3748",
            text_color=self.text_color,
            border_color=self.primary_color,
            border_width=2,
            corner_radius=10
        )
        self.search_entry.pack(side="left", padx=(0, 10))
        self.search_button = ctk.CTkButton(
            self.search_frame,
            text="Buscar",
            fg_color=self.primary_color,
            hover_color="#1E40AF",
            text_color="white",
            corner_radius=8,
            command=self.pesquisar_veiculos
        )
        self.search_button.pack(side="left")

        # Frame da Tabela de Veículos
        self.table_frame = ctk.CTkFrame(self.main_frame, fg_color=self.bg_color)
        self.table_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.table_frame.grid_rowconfigure(0, weight=1)

        # Estilização da Tabela (Treeview) com ttk
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background=self.bg_color,
            fieldbackground=self.bg_color,
            foreground=self.text_color,
            rowheight=35,
            font=("Arial", 12)
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 13, "bold"),
            background=self.secondary_color,
            foreground=self.text_color
        )
        style.map("Treeview", background=[("selected", self.primary_color)])

        self.table = ttk.Treeview(
            self.table_frame,
            columns=("Marca", "Modelo", "Cliente", "Matrícula", "Km", "OBS", "Ações"),
            show="headings"
        )
        self.table.heading("Marca", text="Marca")
        self.table.heading("Modelo", text="Modelo")
        self.table.heading("Cliente", text="Cliente")
        self.table.heading("Matrícula", text="Matrícula")
        self.table.heading("Km", text="Km")
        self.table.heading("OBS", text="Observações")
        self.table.heading("Ações", text="Ações")

        self.table.column("Marca", width=100)
        self.table.column("Modelo", width=100)
        self.table.column("Cliente", width=150)
        self.table.column("Matrícula", width=100)
        self.table.column("Km", width=80)
        self.table.column("OBS", width=200)
        self.table.column("Ações", width=150)

        self.table.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Carregar os dados iniciais na tabela
        self.ver_veiculos()

    def ver_veiculos(self):
        # Dados de exemplo
        veiculos = [
            {"Marca": "Toyota", "Modelo": "Corolla", "Cliente": "João Silva", "Matrícula": "ABC-1234", "Km": 50000, "OBS": "Revisão em dia"},
            {"Marca": "Honda", "Modelo": "Civic", "Cliente": "Maria Oliveira", "Matrícula": "XYZ-5678", "Km": 30000, "OBS": "Troca de óleo recente"},
            {"Marca": "Ford", "Modelo": "Focus", "Cliente": "Carlos Souza", "Matrícula": "DEF-9012", "Km": 45000, "OBS": "Pneus novos"}
        ]

        # Limpar tabela antes de inserir
        for row in self.table.get_children():
            self.table.delete(row)

        # Inserir dados na tabela
        for veiculo in veiculos:
            self.table.insert(
                "",
                "end",
                values=(
                    veiculo["Marca"],
                    veiculo["Modelo"],
                    veiculo["Cliente"],
                    veiculo["Matrícula"],
                    veiculo["Km"],
                    veiculo["OBS"],
                    ""  # Coluna "Ações" (preenchida a seguir)
                )
            )
        self.inserir_acoes_na_tabela()

    def inserir_acoes_na_tabela(self):
        """
        Exemplo simples: define a coluna "Ações" com o texto "Editar | Remover".
        Em uma aplicação real, você pode implementar ações mais complexas (por exemplo, com menus ou pop-ups).
        """
        for item_id in self.table.get_children():
            self.table.set(item_id, "Ações", "Editar | Remover")

    def pesquisar_veiculos(self):
        termo = self.search_entry.get().lower()
        veiculos = [
            {"Marca": "Toyota", "Modelo": "Corolla", "Cliente": "João Silva", "Matrícula": "ABC-1234", "Km": 50000, "OBS": "Revisão em dia"},
            {"Marca": "Honda", "Modelo": "Civic", "Cliente": "Maria Oliveira", "Matrícula": "XYZ-5678", "Km": 30000, "OBS": "Troca de óleo recente"},
            {"Marca": "Ford", "Modelo": "Focus", "Cliente": "Carlos Souza", "Matrícula": "DEF-9012", "Km": 45000, "OBS": "Pneus novos"}
        ]
        resultados = [v for v in veiculos if termo in v["Matrícula"].lower() or termo in v["Cliente"].lower()]

        for row in self.table.get_children():
            self.table.delete(row)

        for veiculo in resultados:
            self.table.insert(
                "",
                "end",
                values=(
                    veiculo["Marca"],
                    veiculo["Modelo"],
                    veiculo["Cliente"],
                    veiculo["Matrícula"],
                    veiculo["Km"],
                    veiculo["OBS"],
                    ""
                )
            )
        self.inserir_acoes_na_tabela()

    # Métodos para a navegação da sidebar (podem ser expandidos conforme a funcionalidade)
    def show_dashboard(self):
        print("Exibindo Dashboard")

    def show_veiculos(self):
         """Abre a view de gerenciamento de veiculos."""
         self.destroy()
         ClientView().mainloop()

    def show_clientes(self):
        print("Exibindo Clientes")

    def show_relatorios(self):
        print("Exibindo Relatórios")
    
    def show_relatorios(self):
        print("Exibindo Relatórios")



if __name__ == "__main__":
    app = CarView()
    app.mainloop()
