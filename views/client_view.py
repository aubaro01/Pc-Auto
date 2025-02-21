import customtkinter as ctk
from tkinter import messagebox
from models.clients import Cliente
import tkinter as tk

class ClientView(ctk.CTk):
        def __init__(self):
            super().__init__()

        
            self.title("Gestão de Clientes")
            self.geometry("1200x800")
            self.resizable(True, True)
            self.configure(bg="#2C3E50")  

        
            self.row_tags = {}
            self.last_hovered = None

            self.label_title = ctk.CTkLabel(
                self, 
                text="📋 Gestão de Clientes", 
                font=("Arial", 30, "bold"), 
                fg_color="#1A252F", 
                text_color="white", 
                corner_radius=10, 
                height=50
            )
            self.label_title.pack(fill="x", pady=(10, 20), padx=20)

            # Frame de Pesquisa e Ações
            self.top_frame = ctk.CTkFrame(self, fg_color="#34495E", corner_radius=10)
            self.top_frame.pack(pady=10, padx=20, fill="x")
            
            self.search_entry = ctk.CTkEntry(
                self.top_frame, 
                placeholder_text="Pesquisar cliente pelo nome...", 
                height=40, 
                corner_radius=10,
                fg_color="#2C3E50",
                text_color="white",
                placeholder_text_color="#BDC3C7"
            )
            self.search_entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)
            
            self.search_button = ctk.CTkButton(
                self.top_frame, 
                text="Pesquisar", 
                fg_color="#2980b9", 
                hover_color="#2471A3", 
                command=lambda: self.pesquisar_cliente(), 
                width=150
            )
            self.search_button.pack(side="left", padx=10, pady=10)
            
            self.action_frame = ctk.CTkFrame(self, fg_color="#2C3E50", corner_radius=10)
            self.action_frame.pack(pady=10, padx=20, fill="x")
            
            button_style = {"width": 150, "height": 50, "corner_radius": 10}
            self.button_add = ctk.CTkButton(
                self.action_frame, 
                text="➕ Adicionar", 
                fg_color="#27ae60", 
                hover_color="#1E8449", 
                command=lambda: self.abrir_janela_adicionar(), 
                **button_style
            )
            self.button_add.grid(row=0, column=0, padx=10, pady=10)
            
            self.button_update = ctk.CTkButton(
                self.action_frame, 
                text="✏️ Atualizar", 
                fg_color="#f39c12", 
                hover_color="#D68910", 
                command=lambda: self.abrir_janela_atualizar(), 
                **button_style
            )
            self.button_update.grid(row=0, column=1, padx=10, pady=10)
            
            self.button_delete = ctk.CTkButton(
                self.action_frame, 
                text="❌ Deletar", 
                fg_color="#e74c3c", 
                hover_color="#C0392B", 
                command=lambda: messagebox.showinfo("Informação", "Utilize o botão ❌ em cada card para deletar o cliente."), 
                **button_style
            )
            self.button_delete.grid(row=0, column=2, padx=10, pady=10)
            
            self.button_view = ctk.CTkButton(
                self.action_frame, 
                text="👁️ Ver Todos", 
                fg_color="#2980b9", 
                hover_color="#2471A3", 
                command=lambda: self.ver_clientes(), 
                **button_style
            )
            self.button_view.grid(row=0, column=3, padx=10, pady=10)
            
            self.button_back = ctk.CTkButton(
                self.action_frame,
                text="Voltar",
                fg_color="#7f8c8d",
                hover_color="#95a5a6",
                command=lambda: self.voltarMain(),
                **button_style
            )
            self.button_back.grid(row=0, column=4, padx=10, pady=10)
            
            self.card_canvas = tk.Canvas(self, bg="#2C3E50", highlightthickness=0)
            self.card_canvas.pack(side="left", fill="both", expand=True, padx=(20,0), pady=20)
            
            self.scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.card_canvas.yview)
            self.scrollbar.pack(side="right", fill="y", pady=20, padx=(0,20))
            
            self.card_canvas.configure(yscrollcommand=self.scrollbar.set)
            self.card_frame = ctk.CTkFrame(self.card_canvas, fg_color="#2C3E50", corner_radius=10)
            self.card_canvas.create_window((0,0), window=self.card_frame, anchor="nw")
            self.card_frame.bind("<Configure>", lambda e: self.card_canvas.configure(scrollregion=self.card_canvas.bbox("all")))
            
        
            self.campos = ["Nome", "NIF", "Email", "Telefone", "Observações"]
            
            self.ver_clientes()


        def render_cards(self, clientes):
            
            for widget in self.card_frame.winfo_children():
                widget.destroy()
            
            # Para cada cliente, cria um card
            for cliente in clientes:
                card = ctk.CTkFrame(self.card_frame, fg_color="#34495E", corner_radius=10)
                card.pack(pady=10, padx=20, fill="x")
                
                info = (f"Nome: {cliente[1]}\n"
                        f"NIF: {cliente[2]}\n"
                        f"Email: {cliente[3]}\n"
                        f"Telefone: {cliente[4]}\n"
                        f"Observações: {cliente[5]}")
                label_info = ctk.CTkLabel(card, text=info, font=("Arial", 12), text_color="white", justify="left")
                label_info.pack(side="left", padx=10, pady=10, fill="x", expand=True)
                
                action_frame = ctk.CTkFrame(card, fg_color="#34495E", corner_radius=10)
                action_frame.pack(side="right", padx=10, pady=10)
                
                btn_update = ctk.CTkButton(
                    action_frame, 
                    text="✏️", 
                    fg_color="#f39c12", 
                    hover_color="#D68910", 
                    command=lambda c=cliente: self.abrir_janela_atualizar_com_cliente(c),
                    width=40
                )
                btn_update.pack(pady=5)
                
                btn_delete = ctk.CTkButton(
                    action_frame, 
                    text="❌", 
                    fg_color="#e74c3c", 
                    hover_color="#C0392B", 
                    command=lambda c=cliente: self.deletar_cliente_por_id(c[0]),
                    width=40
                )
                btn_delete.pack(pady=5)
        
        def abrir_janela_adicionar(self):
            self.janela_adicionar = ctk.CTkToplevel(self)
            self.janela_adicionar.title("Adicionar Cliente")
            self.janela_adicionar.geometry("400x400")
            self.janela_adicionar.resizable(False, False)
            self.janela_adicionar.configure(bg="#2C3E50")
            self.janela_adicionar.transient(self)
            self.janela_adicionar.grab_set()
            self.janela_adicionar.focus_set()
            
            self.entries_add = {}
            for campo in self.campos:
                entry = ctk.CTkEntry(
                    self.janela_adicionar, 
                    placeholder_text=f"Digite o {campo.lower()}", 
                    height=40, 
                    corner_radius=10,
                    fg_color="#34495E",
                    text_color="white",
                    placeholder_text_color="#BDC3C7"
                )
                entry.pack(pady=10, padx=20, fill="x")
                self.entries_add[campo] = entry
            botao_salvar = ctk.CTkButton(
                self.janela_adicionar, 
                text="Salvar", 
                fg_color="#27ae60", 
                hover_color="#1E8449", 
                command=lambda: self.adicionar_cliente()
            )
            botao_salvar.pack(pady=20)
        
        def adicionar_cliente(self):
            if hasattr(self, 'entries_add'):
                dados = {campo: self.entries_add[campo].get() for campo in self.entries_add}
                if all(dados.values()):
                    Cliente.criar_cliente(*dados.values())
                    messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
                    self.janela_adicionar.destroy()
                    self.ver_clientes()
                else:
                    messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        
        def abrir_janela_atualizar_com_cliente(self, cliente):
            self.janela_atualizar = ctk.CTkToplevel(self)
            self.janela_atualizar.title("Atualizar Cliente")
            self.janela_atualizar.geometry("400x400")
            self.janela_atualizar.resizable(False, False)
            self.janela_atualizar.configure(bg="#2C3E50")
            self.janela_atualizar.transient(self)
            self.janela_atualizar.grab_set()
            self.janela_atualizar.focus_set()
            
            self.entries_update = {}
            for i, campo in enumerate(self.campos):
                entry = ctk.CTkEntry(
                    self.janela_atualizar, 
                    placeholder_text=f"Digite o {campo.lower()}", 
                    height=40, 
                    corner_radius=10,
                    fg_color="#34495E",
                    text_color="white",
                    placeholder_text_color="#BDC3C7"
                )
                entry.pack(pady=10, padx=20, fill="x")
                entry.insert(0, cliente[i+1])
                self.entries_update[campo] = entry
            botao_salvar = ctk.CTkButton(
                self.janela_atualizar, 
                text="Salvar", 
                fg_color="#f39c12", 
                hover_color="#D68910", 
                command=lambda: self.atualizar_cliente(cliente[0])
            )
            botao_salvar.pack(pady=20)
        
        def atualizar_cliente(self, id_cliente):
            if hasattr(self, 'entries_update'):
                dados = {campo: self.entries_update[campo].get() for campo in self.entries_update}
                if all(dados.values()):
                    Cliente.atualizar_cliente(id_cliente, *dados.values())
                    messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
                    self.janela_atualizar.destroy()
                    self.ver_clientes()
                else:
                    messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        
        def deletar_cliente_por_id(self, id_cliente):
            Cliente.deletar_cliente(id_cliente)
            messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
            self.ver_clientes()
        
        def ver_clientes(self):
            clientes = Cliente.buscar_todos_clientes()
            self.render_cards(clientes)
        
        def pesquisar_cliente(self):
            query = self.search_entry.get().strip()
            if query:
                resultados = Cliente.pesquisar_cliente(query)
                self.render_cards(resultados)
            else:
                self.ver_clientes()

        def voltarMain(self):
            self.destroy()
            from views.main_app import MainApp  # Importar aqui para evitar importação circular
            MainApp().mainloop()

if __name__ == "__main__":
        app = ClientView()
        app.mainloop()
