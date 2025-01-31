import customtkinter as ctk
from views.client_view import ClientView
from views.car_view import CarView
from views.marcs_view import MarcsView
from models.clients import Cliente
from models.cars import Veiculo
from models.marcs import Marcacoes
from tkinter import messagebox

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pc_Auto - Principal")
        self.geometry("1000x700")  # Tela maior
        self.configure(bg="#2e2e2e")

        self.create_widgets()

    def create_widgets(self):
        """Configura os elementos da interface principal."""
        # Título de boas-vindas
        self.label_welcome = ctk.CTkLabel(
            self,
            text="Bem-vindo ao Pc Auto!",
            font=("Arial", 28, "bold"),
            fg_color="#1f6aa5",
            text_color="white"
        )
        self.label_welcome.pack(pady=20)

        # Frame para os cards
        self.card_frame = ctk.CTkFrame(self, fg_color="#2e2e2e")
        self.card_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Adicionar cards informativos
        self.create_info_cards()

        # Rodapé
        self.footer = ctk.CTkLabel(
            self,
            text="Pc_Auto © 2025",
            font=("Arial", 12),
            fg_color="#1f6aa5",
            text_color="white"
        )
        self.footer.pack(side="bottom", fill="x", pady=10)

        # Configuração do layout da grade para os cards
        for col in range(3):
            self.card_frame.grid_columnconfigure(col, weight=1)

    def create_nav_buttons(self):
        """Cria os botões de navegação na aplicação."""
        buttons = [
            ("Gerenciar Clientes", self.abrir_client_view),
            ("Ver Veículos", self.abrir_car_view),
            ("Ver Marcações", self.abrir_marcs_view)
        ]

        for idx, (text, command) in enumerate(buttons):
            button = ctk.CTkButton(
                self,
                text=text,
                fg_color="#1f6aa5",
                hover_color="#155a8c",
                text_color="white",
                command=command
            )
            button.pack(pady=10, padx=20, fill="x")

    def create_info_cards(self):
        """Cria os cards informativos na interface principal."""
        total_clientes = self.get_total_clientes()
        total_veiculos = self.get_total_veiculos()
        total_marcacoes = self.get_total_marcacoes()

        cards = [
            ("Total de Clientes", total_clientes),
            ("Total de Veículos", total_veiculos),
            ("Total de Marcações", total_marcacoes)
        ]

        for idx, (title, value) in enumerate(cards):
            card = ctk.CTkFrame(self.card_frame, fg_color="#1f6aa5", corner_radius=8)
            card.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

            label_title = ctk.CTkLabel(card, text=title, font=("Arial", 16, "bold"), text_color="white")
            label_title.pack(pady=10)

            label_value = ctk.CTkLabel(card, text=str(value), font=("Arial", 24, "bold"), text_color="white")
            label_value.pack(pady=10)

    def get_total_clientes(self):
        """Retorna o total de clientes cadastrados."""
        return Clients.totalClientes()

    def get_total_veiculos(self):
        """Retorna o total de veículos cadastrados."""
        return Veiculo.total_veiculos()

    def get_total_marcacoes(self):
        """Retorna o total de marcações cadastradas."""
        return Marcacoes.total_marcacoes()

    def abrir_client_view(self):
        """Abre a visualização de gerenciamento de clientes."""
        self.destroy()
        ClientView().mainloop()

    def abrir_car_view(self):
        """Abre a visualização de gerenciamento de veículos."""
        self.destroy()
        CarView().mainloop()

    def abrir_marcs_view(self):
        """Abre a visualização de gerenciamento de marcações."""
        self.destroy()
        MarcsView().mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()