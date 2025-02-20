import customtkinter as ctk
from tkinter import messagebox
from views.client_view import ClientView
from views.marcs_view import MarcsView
from models.cars import Veiculo
from models.clients import Cliente

class CarView(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Gerenciamento de Veículos")
        self.geometry("1200x800")
        self.minsize(1000, 700)
        self.resizable(True, True)

        # Definir cores principais
        self.bg_color = "#1F2937"         # Fundo principal
        self.primary_color = "#3B82F6"      # Cor primária
        self.secondary_color = "#2563EB"    # Cor secundária
        self.text_color = "#F3F4F6"         # Cor do texto

        self.configure(bg=self.bg_color)

        # Layout principal com 2 colunas: Sidebar e Área Principal
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._create_sidebar()
        self._create_main_area()

        # Variável para armazenar todos os veículos (para busca)
        self.veiculos_all = []
        self.veiculos = []

        # Carregar os dados iniciais na tabela
        self.carregar_veiculos()

    def _create_sidebar(self) -> None:
        """Cria a sidebar de navegação."""
        self.sidebar_frame = ctk.CTkFrame(self, width=220, fg_color="#2e2e2e")
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")
        self.sidebar_frame.grid_propagate(False)

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

    def _create_main_area(self) -> None:
        """Cria a área principal da aplicação."""
        self.main_frame = ctk.CTkFrame(self, fg_color=self.bg_color)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
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

        # Barra de Pesquisa e Botão "Adicionar Veículo"
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
        self.search_button.pack(side="left", padx=(0, 10))
        self.add_button = ctk.CTkButton(
            self.search_frame,
            text="Adicionar Veículo",
            fg_color="#10B981",
            hover_color="#059669",
            text_color="white",
            corner_radius=8,
            command=self.abrir_formulario
        )
        self.add_button.pack(side="left")

        # Frame da Tabela de Veículos
        self.table_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color=self.bg_color)
        self.table_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.table_frame.grid_columnconfigure(0, weight=1)

        # Cabeçalho da Tabela
        self.table_header = ctk.CTkFrame(self.table_frame, fg_color=self.secondary_color)
        self.table_header.grid(row=0, column=0, sticky="ew")
        headers = ["Marca", "Modelo", "Cliente", "Matrícula", "Km", "OBS", "Ações"]
        for i, header in enumerate(headers):
            label = ctk.CTkLabel(
                self.table_header,
                text=header,
                font=("Arial", 14, "bold"),
                text_color=self.text_color
            )
            label.grid(row=0, column=i, padx=10, pady=5, sticky="w")
        
        # Container para as linhas da tabela
        self.table_rows_frame = ctk.CTkFrame(self.table_frame, fg_color=self.bg_color)
        self.table_rows_frame.grid(row=1, column=0, sticky="nsew")

    def carregar_veiculos(self) -> None:
        """Carrega os dados dos veículos na tabela."""
        resultados = Veiculo.buscar_todos_veiculos()
        self.veiculos_all = resultados
        self.veiculos = resultados.copy()
        self.atualizar_tabela()

    def atualizar_tabela(self) -> None:
        """Atualiza a tabela com os dados dos veículos."""
        # Limpar as linhas atuais da tabela
        self.table_rows_frame.destroy()
        self.table_rows_frame = ctk.CTkFrame(self.table_frame, fg_color=self.bg_color)
        self.table_rows_frame.grid(row=1, column=0, sticky="nsew")

        for i, veiculo in enumerate(self.veiculos):
            row_frame = ctk.CTkFrame(self.table_rows_frame, fg_color="#2D3748", corner_radius=10)
            row_frame.grid(row=i, column=0, sticky="ew", pady=5, padx=5)

            # Colunas de dados
            for j, key in enumerate(["Marca", "Modelo", "Cliente", "Matrícula", "Km", "OBS"]):
                valor = veiculo.get(key, "")
                label = ctk.CTkLabel(
                    row_frame,
                    text=valor,
                    font=("Arial", 12),
                    text_color=self.text_color
                )
                label.grid(row=0, column=j, padx=10, pady=5, sticky="w")

            # Botões de ação
            actions_frame = ctk.CTkFrame(row_frame, fg_color="transparent")
            actions_frame.grid(row=0, column=6, padx=10, pady=5, sticky="e")

            edit_button = ctk.CTkButton(
                actions_frame,
                text="Editar",
                fg_color=self.primary_color,
                hover_color="#1E40AF",
                text_color="white",
                corner_radius=8,
                width=80,
                command=lambda v=veiculo: self.abrir_formulario(v)
            )
            edit_button.pack(side="left", padx=(0, 5))

            delete_button = ctk.CTkButton(
                actions_frame,
                text="Remover",
                fg_color="#EF4444",
                hover_color="#DC2626",
                text_color="white",
                corner_radius=8,
                width=80,
                command=lambda v=veiculo: self.remover_veiculo(v)
            )
            delete_button.pack(side="left")

    def abrir_formulario(self, veiculo: dict = None) -> None:
        """Abre o formulário para adicionar ou editar um veículo."""
        self.formulario = ctk.CTkToplevel(self)
        self.formulario.title("Adicionar Veículo" if not veiculo else "Editar Veículo")
        self.formulario.geometry("400x400")
        self.formulario.resizable(False, False)
        self.formulario.grab_set()

        # Carregar marcas, modelos e clientes da base de dados
        marcas = Veiculo.buscar_marcas()
        clientes = Cliente.buscar_clientes()

        if not marcas or not clientes:
            messagebox.showerror("Erro", "Não foi possível carregar os dados necessários.")
            self.formulario.destroy()
            return

        # Campos do Formulário
        self.campos = ["Marca", "Modelo", "Cliente", "Matrícula", "Km", "OBS"]
        self.entries = {}
        for i, campo in enumerate(self.campos):
            label = ctk.CTkLabel(self.formulario, text=campo, font=("Arial", 12), text_color=self.text_color)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            if campo == "Marca":
                self.marca_combobox = ctk.CTkComboBox(
                    self.formulario,
                    values=[marca["Nome"] for marca in marcas],
                    command=self.carregar_modelos
                )
                self.marca_combobox.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
                self.entries[campo] = self.marca_combobox
            elif campo == "Modelo":
                self.modelo_combobox = ctk.CTkComboBox(self.formulario, values=[])
                self.modelo_combobox.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
                self.entries[campo] = self.modelo_combobox
            elif campo == "Cliente":
                self.cliente_combobox = ctk.CTkComboBox(
                    self.formulario,
                    values=[cliente["NomeCliente"] for cliente in clientes]
                )
                self.cliente_combobox.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
                self.entries[campo] = self.cliente_combobox
            else:
                entry = ctk.CTkEntry(self.formulario, width=250)
                entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
                self.entries[campo] = entry

        # Se estiver editando, preenche os campos com os dados existentes;
        # Caso contrário, define os valores padrão com base no primeiro item de cada lista.
        if veiculo:
            self.marca_combobox.set(veiculo.get("Marca", ""))
            self.carregar_modelos(veiculo.get("Marca", ""))
            self.modelo_combobox.set(veiculo.get("Modelo", ""))
            self.cliente_combobox.set(veiculo.get("Cliente", ""))
            self.entries["Matrícula"].insert(0, veiculo.get("Matricula", ""))
            self.entries["Km"].insert(0, str(veiculo.get("Km", "")))
            self.entries["OBS"].insert(0, veiculo.get("OBS", ""))
        else:
            # Define os valores padrão para um novo veículo
            marcas_valores = self.marca_combobox.cget("values")
            if marcas_valores:
                self.marca_combobox.set(marcas_valores[0])
                self.carregar_modelos(marcas_valores[0])
                modelos_valores = self.modelo_combobox.cget("values")
                if modelos_valores:
                    self.modelo_combobox.set(modelos_valores[0])
            clientes_valores = self.cliente_combobox.cget("values")
            if clientes_valores:
                self.cliente_combobox.set(clientes_valores[0])

        # Botões de Salvar e Cancelar
        button_frame = ctk.CTkFrame(self.formulario, fg_color="transparent")
        button_frame.grid(row=len(self.campos), column=0, columnspan=2, pady=10)

        save_button = ctk.CTkButton(
            button_frame,
            text="Salvar",
            fg_color="#10B981",
            hover_color="#059669",
            text_color="white",
            corner_radius=8,
            command=lambda: self.salvar_veiculo(veiculo)
        )
        save_button.pack(side="left", padx=(0, 10))

        cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancelar",
            fg_color="#EF4444",
            hover_color="#DC2626",
            text_color="white",
            corner_radius=8,
            command=self.formulario.destroy
        )
        cancel_button.pack(side="left")

    def carregar_modelos(self, marca_nome: str) -> None:
        """Carrega os modelos da marca selecionada."""
        marcas = Veiculo.buscar_marcas()
        marca_id = next((marca["Marca_id"] for marca in marcas if marca["Nome"] == marca_nome), None)
        if marca_id:
            modelos = Veiculo.buscar_modelos_por_marca(marca_id)
            self.modelo_combobox.configure(values=[modelo["Nome"] for modelo in modelos])
        else:
            self.modelo_combobox.configure(values=[])

    def salvar_veiculo(self, veiculo: dict = None) -> None:
        """Salva um novo veículo ou atualiza um existente."""
        marcas = Veiculo.buscar_marcas()
        modelos = Veiculo.buscar_modelos_por_marca(
            next((marca["Marca_id"] for marca in marcas if marca["Nome"] == self.marca_combobox.get()), None)
        )
        clientes = Cliente.buscar_clientes()

        marca_id = next((marca["Marca_id"] for marca in marcas if marca["Nome"] == self.marca_combobox.get()), None)
        modelo_id = next((modelo["Modelo_id"] for modelo in modelos if modelo["Nome"] == self.modelo_combobox.get()), None)
        cliente_id = next((cliente["idCliente"] for cliente in clientes if cliente["NomeCliente"] == self.cliente_combobox.get()), None)

        matricula = self.entries["Matrícula"].get().strip()
        km = self.entries["Km"].get().strip()
        obs = self.entries["OBS"].get().strip()

        if all([marca_id, modelo_id, cliente_id, matricula, km]):
            try:
                km_int = int(km)
            except ValueError:
                messagebox.showwarning("Erro", "O campo Km deve ser um número.")
                return

            if veiculo:
                Veiculo.atualizar_veiculo(
                    veiculo["Veiculo_id"], marca_id, modelo_id, cliente_id, matricula, km_int, obs
                )
            else:
                Veiculo.criar_veiculo(marca_id, modelo_id, cliente_id, matricula, km_int, obs)
            self.carregar_veiculos()
            self.formulario.destroy()
            messagebox.showinfo("Sucesso", "Veículo salvo com sucesso!")
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")

    def remover_veiculo(self, veiculo: dict) -> None:
        """Remove um veículo da lista."""
        confirm = messagebox.askyesno("Remover", "Tem certeza que deseja remover este veículo?")
        if confirm:
            Veiculo.deletar_veiculo(veiculo["Veiculo_id"])
            self.carregar_veiculos()
            messagebox.showinfo("Sucesso", "Veículo removido com sucesso!")

    def pesquisar_veiculos(self) -> None:
        """Filtra os veículos na tabela com base no termo de pesquisa."""
        termo = self.search_entry.get().lower().strip()
        if termo == "":
            self.veiculos = self.veiculos_all.copy()
        else:
            self.veiculos = [
                v for v in self.veiculos_all 
                if termo in v.get("Matricula", "").lower() or termo in v.get("Cliente", "").lower()
            ]
        self.atualizar_tabela()

    def show_dashboard(self) -> None:
        """Navega para o dashboard principal."""
        self.destroy()
        from views.main_app import MainApp  # Importação local para evitar circularidade
        MainApp().mainloop()

    def show_veiculos(self) -> None:
        """Recarrega a view de veículos."""
        self.destroy()
        CarView().mainloop()

    def show_clientes(self) -> None:
        """Exibe a view de gerenciamento de clientes."""
        self.destroy()
        ClientView().mainloop()

    def show_relatorios(self) -> None:
        """Exibe a view de relatórios."""
        self.destroy()
        from views.carRelatorio_view import CarRelatorioView 
        CarRelatorioView().mainloop()

if __name__ == "__main__":
    app = CarView()
    app.mainloop()
