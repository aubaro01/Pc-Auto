from datetime import datetime, date
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry
from controllers.marcs_controller import MarcsController
from models.marcs import Marcacoes


# Melhorar interface, adicionar acessibilidade 

class MarcsView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Marcações")
        self.geometry("1000x700")
        self.resizable(True, True)

        # Layout Principal
        self.configure(bg="#2e2e2e")

        # Título Principa
        self.label_title = ctk.CTkLabel(self, text="Gerenciamento de Marcações", font=("Arial", 26, "bold"), fg_color="#1f6aa5", text_color="white")
        self.label_title.pack(fill="x", pady=(0, 20))

        # Barra de Pesquisa
        self.search_frame = ctk.CTkFrame(self, fg_color="#2e2e2e")
        self.search_frame.pack(pady=10, padx=20, fill="x")

        self.search_label = ctk.CTkLabel(self.search_frame, text="Pesquisar:", font=("Arial", 14), fg_color="#2e2e2e", text_color="white")
        self.search_label.grid(row=0, column=0, padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self.search_frame, width=200, fg_color="#1f6aa5", text_color="white", border_color="#1f6aa5", border_width=2)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = ctk.CTkButton(self.search_frame, text="Buscar", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.pesquisar_marcacoes)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        # Botão Voltar ao Menu
        self.back_button = ctk.CTkButton(self.search_frame, text="Voltar ao Menu", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.voltar_ao_menu)
        self.back_button.grid(row=0, column=3, padx=10, pady=10)

        # Botão Adicionar Marcação
        self.add_button = ctk.CTkButton(self.search_frame, text="Adicionar Marcação", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.adicionar_marcacao)
        self.add_button.grid(row=0, column=4, padx=10, pady=10)

        # Frame para os cartões de marcações
        self.cards_frame = ctk.CTkFrame(self, fg_color="#2e2e2e")
        self.cards_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.ver_marcacoes()

    def ver_marcacoes(self):
        marcacoes = MarcsController.buscar_todas_marcacoes()
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        for idx, marcacao in enumerate(marcacoes):
            self.criar_cartao_marcacao(marcacao, idx)

    def criar_cartao_marcacao(self, marcacao, idx):
        card = ctk.CTkFrame(self.cards_frame, fg_color="#1f6aa5", corner_radius=8, width=900, height=950)
        card.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

        label_data = ctk.CTkLabel(card, text=f"Data: {marcacao['Data_marc']}", font=("Arial", 12), text_color="white")
        label_data.grid(row=0, column=0, padx=5, pady=2, sticky="w")

        label_tipo = ctk.CTkLabel(card, text=f"Tipo de Trabalho: {marcacao['Tipo_Trabalho']}", font=("Arial", 12), text_color="white")
        label_tipo.grid(row=1, column=0, padx=5, pady=2, sticky="w")

        label_veiculo = ctk.CTkLabel(card, text=f"Veículo: {marcacao['Veiculo']}", font=("Arial", 12), text_color="white")
        label_veiculo.grid(row=2, column=0, padx=5, pady=2, sticky="w")

        label_cliente = ctk.CTkLabel(card, text=f"Cliente: {marcacao['Cliente']}", font=("Arial", 12), text_color="white")
        label_cliente.grid(row=3, column=0, padx=5, pady=2, sticky="w")

        label_estado = ctk.CTkLabel(card, text=f"Estado: {marcacao['Estado']}", font=("Arial", 12), text_color="white")
        label_estado.grid(row=4, column=0, padx=5, pady=2, sticky="w")

        edit_button = ctk.CTkButton(card, text="Editar", fg_color="#155a8c", hover_color="#0d3a5c", text_color="white", command=lambda: self.editar_marcacao(marcacao['Marcacao_id']))
        edit_button.grid(row=0, column=1, padx=5, pady=2, sticky="e")

        delete_button = ctk.CTkButton(card, text="Remover", fg_color="#155a8c", hover_color="#0d3a5c", text_color="white", command=lambda: self.remover_marcacao(marcacao['Marcacao_id']))
        delete_button.grid(row=1, column=1, padx=5, pady=2, sticky="e")

    def pesquisar_marcacoes(self):
        termo_pesquisa = self.search_entry.get().lower()
        marcacoes = MarcsController.buscar_todas_marcacoes()
        resultados = [marcacao for marcacao in marcacoes if termo_pesquisa in marcacao["Veiculo"].lower() or termo_pesquisa in marcacao["Cliente"].lower()]
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        for idx, marcacao in enumerate(resultados):
            self.criar_cartao_marcacao(marcacao, idx)

    def adicionar_marcacao(self):
        self.add_window = ctk.CTkToplevel(self)
        self.add_window.title("Adicionar Marcação")
        self.add_window.geometry("400x400")

        label_data = ctk.CTkLabel(self.add_window, text="Data (YYYY-MM-DD):", font=("Arial", 12))
        label_data.pack(pady=10)
        self.entry_data = DateEntry(self.add_window, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.entry_data.pack(pady=10)

        label_tipo = ctk.CTkLabel(self.add_window, text="Tipo de Trabalho:", font=("Arial", 12))
        label_tipo.pack(pady=10)
        self.entry_tipo = ctk.CTkComboBox(self.add_window, values=[tipo['Marcacao'] for tipo in Marcacoes.buscar_tipos_trabalho()], width=200)
        self.entry_tipo.pack(pady=10)

        label_veiculo = ctk.CTkLabel(self.add_window, text="Veículo:", font=("Arial", 12))
        label_veiculo.pack(pady=10)
        self.entry_veiculo = ctk.CTkEntry(self.add_window, width=200)
        self.entry_veiculo.pack(pady=10)

        label_cliente = ctk.CTkLabel(self.add_window, text="Cliente:", font=("Arial", 12))
        label_cliente.pack(pady=10)
        self.entry_cliente = ctk.CTkEntry(self.add_window, width=200)
        self.entry_cliente.pack(pady=10)

        label_estado = ctk.CTkLabel(self.add_window, text="Estado:", font=("Arial", 12))
        label_estado.pack(pady=10)
        self.entry_estado = ctk.CTkComboBox(self.add_window, values=[estado['Estado'] for estado in Marcacoes.buscar_estados()], width=200)
        self.entry_estado.pack(pady=10)

        add_button = ctk.CTkButton(self.add_window, text="Adicionar", fg_color="#1f6aa5", hover_color="#155a8c", text_color="white", command=self.salvar_marcacao)
        add_button.pack(pady=20)

    def salvar_marcacao(self):
        data_marc = self.entry_data.get()
        tipo_trabalho = self.entry_tipo.get()
        veiculo = self.entry_veiculo.get()
        cliente = self.entry_cliente.get()
        estado = self.entry_estado.get()

        if data_marc and tipo_trabalho and veiculo and cliente and estado:
            tipo_trabalho_id = next(tipo['id_TipoMarc'] for tipo in Marcacoes.buscar_tipos_trabalho() if tipo['Marcacao'] == tipo_trabalho)
            estado_id = next(estado['Estado'] for estado in Marcacoes.buscar_estados() if estado['Estado'] == estado)
            MarcsController.criar_marcacao(data_marc, tipo_trabalho_id, veiculo, estado_id)
            self.add_window.destroy()
            self.ver_marcacoes()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def editar_marcacao(self, marcacao_id):
        print(f"Ação: Editar Marcação {marcacao_id}")

    def remover_marcacao(self, marcacao_id):
        confirm = messagebox.askyesno("Confirmar", "Deseja realmente remover esta marcação?")
        if confirm:
            MarcsController.deletar_marcacao(marcacao_id)
            self.ver_marcacoes()

    def voltar_ao_menu(self):
        """Volta ao menu principal."""
        self.destroy()
        from main import MainApp  # Importar aqui para evitar importação circular
        MainApp().mainloop()

if __name__ == "__main__":
    app = MarcsView()
    app.mainloop()