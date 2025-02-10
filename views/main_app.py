import customtkinter as ctk
from views.client_view import ClientView
from views.car_view import CarView
from views.marcs_view import MarcsView
from models.clients import Cliente
from models.cars import Veiculo
from models.marcs import Marcacoes
from tkinter import messagebox
from datetime import datetime

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pc Auto - Principal")
        self.geometry("1200x800")
        self.configure(bg="#1e1e1e")
        self.create_widgets()

    def create_widgets(self):
        # Configura o layout principal com 2 colunas: Sidebar e Área de Conteúdo
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ===== Sidebar de Navegação =====
        self.sidebar_frame = ctk.CTkFrame(self, width=220, fg_color="#2e2e2e")
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")
        self.sidebar_frame.grid_propagate(False)

        self.sidebar_title = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Menu", 
            font=("Arial", 20, "bold"),
            text_color="white"
        )
        self.sidebar_title.pack(pady=20)

        nav_buttons = [
            ("Dashboard", self.show_dashboard),
            ("Gerenciar Clientes", self.abrir_client_view),
            ("Ver Veículos", self.abrir_car_view),
            ("Ver Marcações", self.abrir_marcs_view),
            ("Logout", self.logout)
        ]

        for text, command in nav_buttons:
            button = ctk.CTkButton(
                self.sidebar_frame,
                text=text,
                command=command,
                fg_color="#1f6aa5",
                hover_color="#155a8c",
                text_color="white",
                corner_radius=10
            )
            button.pack(pady=10, padx=20, fill="x")

        # ===== Área Principal =====
        self.main_frame = ctk.CTkFrame(self, fg_color="#1F2937")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

        # Header com mensagem de boas-vindas
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="#2563EB", corner_radius=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.label_welcome = ctk.CTkLabel(
            self.header_frame,
            text="Bem-vindo ao Pc Auto!",
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        self.label_welcome.pack(pady=20, padx=20)

        # Dashboard: Cards informativos
        self.dashboard_frame = ctk.CTkFrame(self.main_frame, fg_color="#1F2937")
        self.dashboard_frame.grid(row=1, column=0, sticky="ew", pady=10, padx=10)
        self.dashboard_frame.grid_columnconfigure((0, 1, 2), weight=1)

        total_clientes = self.get_total_clientes()
        total_veiculos = self.get_total_veiculos()
        total_marcacoes = self.get_total_marcacoes()

        # Card para Total de Clientes
        card_clientes = ctk.CTkFrame(self.dashboard_frame, fg_color="#1f6aa5", corner_radius=12)
        card_clientes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        label_clientes = ctk.CTkLabel(
            card_clientes,
            text="Total de Clientes",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        label_clientes.pack(pady=(20, 5))
        value_clientes = ctk.CTkLabel(
            card_clientes,
            text=str(total_clientes),
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        value_clientes.pack(pady=(0,20))

        # Card para Total de Veículos
        card_veiculos = ctk.CTkFrame(self.dashboard_frame, fg_color="#1f6aa5", corner_radius=12)
        card_veiculos.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        label_veiculos = ctk.CTkLabel(
            card_veiculos,
            text="Total de Veículos",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        label_veiculos.pack(pady=(20, 5))
        value_veiculos = ctk.CTkLabel(
            card_veiculos,
            text=str(total_veiculos),
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        value_veiculos.pack(pady=(0,20))

        # Card para Total de Marcações
        card_marcacoes = ctk.CTkFrame(self.dashboard_frame, fg_color="#1f6aa5", corner_radius=12)
        card_marcacoes.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        label_marcacoes = ctk.CTkLabel(
            card_marcacoes,
            text="Total de Marcações",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        label_marcacoes.pack(pady=(20, 5))
        value_marcacoes = ctk.CTkLabel(
            card_marcacoes,
            text=str(total_marcacoes),
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        value_marcacoes.pack(pady=(0,20))

        # Espaço para conteúdo adicional (ex: tabelas, gráficos etc.)
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="#1F2937")
        self.content_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0,10))

        # Adiciona marcações do dia
        self.add_marcacoes_do_dia()

        # ===== Footer =====
        self.footer = ctk.CTkLabel(
            self,
            text="Pc_Auto © 2025",
            font=("Arial", 12),
            fg_color="#1f6aa5",
            text_color="white"
        )
        self.footer.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10, padx=10)

    def get_total_clientes(self):
        """Retorna o total de clientes cadastrados."""
        return Cliente.totalClientes()

    def get_total_veiculos(self):
        """Retorna o total de veículos cadastrados."""
        return Veiculo.totalVeiculos()

    def get_total_marcacoes(self):
        """Retorna o total de marcações cadastradas."""
        return Marcacoes.totalMarcacoes()

    def abrir_client_view(self):
        """Abre a view de gerenciamento de clientes."""
        self.destroy()
        ClientView().mainloop()

    def abrir_car_view(self):
        """Abre a view de gerenciamento de veículos."""
        self.destroy()
        CarView().mainloop()

    def abrir_marcs_view(self):
        """Abre a view de gerenciamento de marcações."""
        self.destroy()
        MarcsView().mainloop()

    def logout(self):
        """Realiza o logout da aplicação."""
        if messagebox.askokcancel("Logout", "Deseja realmente sair?"):
            self.destroy()

    def show_dashboard(self):
        """Exibe (ou atualiza) o dashboard."""
        print("Exibindo Dashboard")
        # Você pode implementar uma atualização dos cards se necessário.

    def add_marcacoes_do_dia(self):
        """Adiciona as marcações do dia abaixo dos cards informativos."""
        hoje = datetime.now().date()

        # Dados de exemplo
        marcacoes_do_dia = [
            {
                'Data_marc': datetime(2023, 10, 10, 9, 0),
                'Tipo_Trabalho': 'Revisão',
                'Veiculo': 'Carro A',
                'Cliente': 'Cliente 1',
                'Estado': 'Pendente'
            },
            {
                'Data_marc': datetime(2023, 10, 10, 11, 0),
                'Tipo_Trabalho': 'Troca de Óleo',
                'Veiculo': 'Carro B',
                'Cliente': 'Cliente 2',
                'Estado': 'Concluído'
            },
            {
                'Data_marc': datetime(2023, 10, 10, 14, 0),
                'Tipo_Trabalho': 'Alinhamento',
                'Veiculo': 'Carro C',
                'Cliente': 'Cliente 3',
                'Estado': 'Em Andamento'
            }
        ]

        if marcacoes_do_dia:
            label_marcacoes_do_dia = ctk.CTkLabel(
                self.content_frame,
                text="Marcações do Dia",
                font=("Arial", 20, "bold"),
                text_color="white"
            )
            label_marcacoes_do_dia.pack(pady=10)

            for marcacao in marcacoes_do_dia:
                marcacao_text = f"{marcacao['Data_marc'].strftime('%H:%M')} - {marcacao['Tipo_Trabalho']} - {marcacao['Veiculo']} - {marcacao['Cliente']} - {marcacao['Estado']}"
                label_marcacao = ctk.CTkLabel(
                    self.content_frame,
                    text=marcacao_text,
                    font=("Arial", 14),
                    text_color="white"
                )
                label_marcacao.pack(pady=5)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()