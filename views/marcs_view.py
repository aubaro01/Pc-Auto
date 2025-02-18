from datetime import datetime, date, timedelta
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry
from controllers.marcs_controller import MarcsController
from models.marcs import Marcacoes

class MarcsView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Marcações")
        self.geometry("1000x700")
        self.resizable(True, True)

        # Layout Principal
        self.configure(bg="#2e2e2e")

        # Título Principal
        self.label_title = ctk.CTkLabel(
            self, 
            text="Gerenciamento de Marcações", 
            font=("Arial", 26, "bold"), 
            fg_color="#1f6aa5", 
            text_color="white"
        )
        self.label_title.pack(fill="x", pady=(0, 20))

        # Barra de Pesquisa
        self.search_frame = ctk.CTkFrame(self, fg_color="#2e2e2e")
        self.search_frame.pack(pady=10, padx=20, fill="x")

        self.search_label = ctk.CTkLabel(
            self.search_frame, 
            text="Pesquisar:", 
            font=("Arial", 14), 
            fg_color="#2e2e2e", 
            text_color="white"
        )
        self.search_label.grid(row=0, column=0, padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(
            self.search_frame, 
            width=200, 
            fg_color="#1f6aa5", 
            text_color="white", 
            border_color="#1f6aa5", 
            border_width=2
        )
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = ctk.CTkButton(
            self.search_frame, 
            text="Buscar", 
            fg_color="#1f6aa5", 
            hover_color="#155a8c", 
            text_color="white", 
            command=self.pesquisar_marcacoes
        )
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        # Botão Voltar ao Menu
        self.back_button = ctk.CTkButton(
            self.search_frame, 
            text="Voltar ao Menu", 
            fg_color="#1f6aa5", 
            hover_color="#155a8c", 
            text_color="white", 
            command=self.voltar_ao_menu
        )
        self.back_button.grid(row=0, column=3, padx=10, pady=10)

        # Botão Adicionar Marcação
        self.add_button = ctk.CTkButton(
            self.search_frame, 
            text="Adicionar Marcação", 
            fg_color="#1f6aa5", 
            hover_color="#155a8c", 
            text_color="white", 
            command=self.adicionar_marcacao
        )
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

        edit_button = ctk.CTkButton(
            card, 
            text="Editar", 
            fg_color="#155a8c", 
            hover_color="#0d3a5c", 
            text_color="white", 
            command=lambda: self.editar_marcacao(marcacao['Marcacao_id'])
        )
        edit_button.grid(row=0, column=1, padx=5, pady=2, sticky="e")

        delete_button = ctk.CTkButton(
            card, 
            text="Remover", 
            fg_color="#155a8c", 
            hover_color="#0d3a5c", 
            text_color="white", 
            command=lambda: self.remover_marcacao(marcacao['Marcacao_id'])
        )
        delete_button.grid(row=1, column=1, padx=5, pady=2, sticky="e")

    def pesquisar_marcacoes(self):
        termo_pesquisa = self.search_entry.get().lower()
        marcacoes = MarcsController.buscar_todas_marcacoes()
        resultados = [
            marcacao for marcacao in marcacoes 
            if termo_pesquisa in marcacao["Veiculo"].lower() or termo_pesquisa in marcacao["Cliente"].lower()
        ]
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        for idx, marcacao in enumerate(resultados):
            self.criar_cartao_marcacao(marcacao, idx)

    def adicionar_marcacao(self):
        self.add_window = ctk.CTkToplevel(self)
        self.add_window.title("Adicionar Marcação")
        self.add_window.geometry("400x600")

        # Customização avançada da seleção de data:
        label_data = ctk.CTkLabel(self.add_window, text="Data (YYYY-MM-DD):", font=("Arial", 12))
        label_data.pack(pady=10)
        # Define a data mínima como hoje e a máxima como um ano a partir de hoje
        max_date = date.today().replace(year=date.today().year + 1)
        self.entry_data = DateEntry(
            self.add_window,
            width=16,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='yyyy-mm-dd',
            mindate=date.today(),
            maxdate=max_date
        )
        self.entry_data.set_date(date.today())
        self.entry_data.pack(pady=10)

        # Seleção de horário usando ComboBoxes para horas e minutos
        label_hora = ctk.CTkLabel(self.add_window, text="Hora:", font=("Arial", 12))
        label_hora.pack(pady=10)
        self.hour_combobox = ctk.CTkComboBox(self.add_window, values=[f"{h:02d}" for h in range(9, 20)], width=80)
        self.hour_combobox.pack(pady=5)

        label_minuto = ctk.CTkLabel(self.add_window, text="Minutos:", font=("Arial", 12))
        label_minuto.pack(pady=10)
        self.minute_combobox = ctk.CTkComboBox(self.add_window, values=[f"{m:02d}" for m in range(0, 60, 15)], width=80)
        self.minute_combobox.pack(pady=5)

        label_tipo = ctk.CTkLabel(self.add_window, text="Tipo de Trabalho:", font=("Arial", 12))
        label_tipo.pack(pady=10)
        self.entry_tipo = ctk.CTkComboBox(
            self.add_window, 
            values=[tipo['Marcacao'] for tipo in Marcacoes.buscar_tipos_trabalho()], 
            width=200
        )
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
        self.entry_estado = ctk.CTkComboBox(
            self.add_window, 
            values=[estado['Estado'] for estado in Marcacoes.buscar_estados()], 
            width=200
        )
        self.entry_estado.pack(pady=10)

        add_button = ctk.CTkButton(
            self.add_window, 
            text="Adicionar", 
            fg_color="#1f6aa5", 
            hover_color="#155a8c", 
            text_color="white", 
            command=self.salvar_marcacao
        )
        add_button.pack(pady=20)

    def salvar_marcacao(self):
        data_marc = self.entry_data.get()
        hour = self.hour_combobox.get()
        minute = self.minute_combobox.get()
        hora_marc = f"{hour}:{minute}"
        tipo_trabalho = self.entry_tipo.get()
        veiculo = self.entry_veiculo.get()
        cliente = self.entry_cliente.get()
        estado_value = self.entry_estado.get()

        # Verifica se a data é um sábado e se a hora é maior que 13:00
        data_obj = datetime.strptime(data_marc, '%Y-%m-%d').date()
        if data_obj.weekday() == 5 and int(hour) >= 13:
            messagebox.showerror("Erro", "Marcações aos sábados só podem ser feitas até as 13:00.")
            return

        if data_marc and hour and minute and tipo_trabalho and veiculo and cliente and estado_value:
            data_hora_marc = f"{data_marc} {hora_marc}"
            tipo_trabalho_id = next(
                tipo['id_TipoMarc'] 
                for tipo in Marcacoes.buscar_tipos_trabalho() 
                if tipo['Marcacao'] == tipo_trabalho
            )
            # Certifique-se de que o dicionário retornado por buscar_estados() contenha a chave desejada.
            estado_id = next(
                item['Estado'] 
                for item in Marcacoes.buscar_estados() 
                if item['Estado'] == estado_value
            )
            MarcsController.criar_marcacao(data_hora_marc, tipo_trabalho_id, veiculo, estado_id)
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
        self.destroy()
        from views.main_app import MainApp  # Importação tardia para evitar circularidade
        MainApp().mainloop()

if __name__ == "__main__":
    app = MarcsView()
    app.mainloop()