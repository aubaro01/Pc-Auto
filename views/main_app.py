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
        self.title("Pc Auto - Principal")
        self.geometry("1000x700")  # Tela maior
        self.configure(bg="#1e1e1e")  # Fundo mais escuro

        self.create_widgets()

    def create_widgets(self):
        """Configura os elementos da interface principal."""
        # Título de boas-vindas
        self.label_welcome = ctk.CTkLabel(
            self,
            text="Bem-vindo ao Pc Auto!",
            font=("Arial", 28, "bold"),
            text_color="white",
            corner_radius=10
        )
        self.label_welcome.pack(pady=20, padx=20, fill="x")

        # Frame principal para navegação e cards
        self.main_frame = ctk.CTkFrame(self, fg_color="#2e2e2e")
        self.main_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Dividindo o layout em duas colunas
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)

        # Menu lateral
        self.create_nav_buttons()

        # Frame para os cards informativos
        self.card_frame = ctk.CTkFrame(self.main_frame, fg_color="#333333")
        self.card_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

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

    def create_nav_buttons(self):
        """Cria os botões de navegação na aplicação."""
        nav_frame = ctk.CTkFrame(self.main_frame, fg_color="#1f6aa5")
        nav_frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        buttons = [
            ("Gerenciar Clientes", self.abrir_client_view),
            ("Ver Veículos", self.abrir_car_view),
            ("Ver Marcações", self.abrir_marcs_view),
            ("Logout", self.logout)
        ]

        for text, command in buttons:
            button = ctk.CTkButton(
                nav_frame,
                text=text,
                fg_color="#1f6aa5",
                hover_color="#155a8c",
                text_color="white",
                corner_radius=10,
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
            card = ctk.CTkFrame(self.card_frame, fg_color="#1f6aa5", corner_radius=12)
            card.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

            label_title = ctk.CTkLabel(card, text=title, font=("Arial", 16, "bold"), text_color="white")
            label_title.pack(pady=10)

            label_value = ctk.CTkLabel(card, text=str(value), font=("Arial", 24, "bold"), text_color="white")
            label_value.pack(pady=10)

        self.card_frame.grid_columnconfigure((0, 1, 2), weight=1)

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
        """Abre a visualização de gerenciamento de clientes."""
        self.destroy()
        client_view().mainloop()

    def abrir_car_view(self):
        """Abre a visualização de gerenciamento de veículos."""
        self.destroy()
        car_view().mainloop()
    
    def logout(self):
        """Realiza o logout do usuário."""
        if messagebox.askokcancel("Logout", "Deseja realmente sair?"):
            self.destroy()

    def abrir_marcs_view(self):
        """Abre a visualização de gerenciamento de marcações."""
        self.destroy()
        marcs_view().mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()