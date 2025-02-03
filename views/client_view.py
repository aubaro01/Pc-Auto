import customtkinter as ctk
from tkinter import messagebox
from models.clients import Cliente
import tkinter as tk
from tkinter import ttk


# Melhorar a forma que se vê os clientes, adicionar formas de ordenação ( clientes com mais marcs...). 
# Melhorar o campo de pesquisa, a tabela de user. Corrigir a função de edit

class ClientView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Clientes")
        self.geometry("1000x700")
        self.resizable(False, False)

        # Layout Principal
        self.configure(bg="#f9f9f9")

        # Título Principal
        self.label_title = ctk.CTkLabel(self, text="Gerenciamento de Clientes", font=("Arial", 26, "bold"), fg_color="#1f6aa5", text_color="white")
        self.label_title.pack(fill="x", pady=(0, 20))

        # Frame dos Botões
        self.button_frame = ctk.CTkFrame(self, fg_color="#ffffff")
        self.button_frame.pack(pady=10, padx=20, fill="x")

        self.button_add = ctk.CTkButton(self.button_frame, text="Adicionar Cliente", fg_color="#1f6aa5", hover_color="#155a8c", command=self.adicionar_cliente)
        self.button_add.grid(row=0, column=0, padx=10, pady=10)

        self.button_update = ctk.CTkButton(self.button_frame, text="Atualizar Cliente", fg_color="#1f6aa5", hover_color="#155a8c", command=self.atualizar_cliente)
        self.button_update.grid(row=0, column=1, padx=10, pady=10)

        self.button_delete = ctk.CTkButton(self.button_frame, text="Deletar Cliente", fg_color="#1f6aa5", hover_color="#155a8c", command=self.deletar_cliente)
        self.button_delete.grid(row=0, column=2, padx=10, pady=10)

        self.button_view = ctk.CTkButton(self.button_frame, text="Ver Clientes", fg_color="#1f6aa5", hover_color="#155a8c", command=self.ver_clientes)
        self.button_view.grid(row=0, column=3, padx=10, pady=10)

        # Formulário
        self.frame_form = ctk.CTkFrame(self, fg_color="#ffffff")
        self.frame_form.pack(pady=10, padx=20, fill="x")

        self.entry_nome = ctk.CTkEntry(self.frame_form, placeholder_text="Nome", height=40, corner_radius=8)
        self.entry_nome.pack(pady=5, padx=10, fill="x")

        self.entry_nif = ctk.CTkEntry(self.frame_form, placeholder_text="NIF", height=40, corner_radius=8)
        self.entry_nif.pack(pady=5, padx=10, fill="x")

        self.entry_email = ctk.CTkEntry(self.frame_form, placeholder_text="Email", height=40, corner_radius=8)
        self.entry_email.pack(pady=5, padx=10, fill="x")

        self.entry_tel = ctk.CTkEntry(self.frame_form, placeholder_text="Telefone", height=40, corner_radius=8)
        self.entry_tel.pack(pady=5, padx=10, fill="x")

        self.entry_obs = ctk.CTkEntry(self.frame_form, placeholder_text="Observações", height=40, corner_radius=8)
        self.entry_obs.pack(pady=5, padx=10, fill="x")

        # Tabela
        self.frame_table = ctk.CTkFrame(self, fg_color="#ffffff")
        self.frame_table.pack(pady=10, padx=20, fill="both", expand=True)

        # Estilo da Tabela
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Arial", 12), rowheight=40, background="#f9f9f9", fieldbackground="#f9f9f9", foreground="#333333", bordercolor="#e0e0e0")
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#1f6aa5", foreground="white", bordercolor="#e0e0e0")
        style.map("Treeview", background=[("selected", "#d4e4fa")])

        self.table = ttk.Treeview(self.frame_table, columns=("Nome", "NIF", "Email", "Telefone", "Observações"), show="headings")
        self.table.heading("Nome", text="Nome")
        self.table.heading("NIF", text="NIF")
        self.table.heading("Email", text="Email")
        self.table.heading("Telefone", text="Telefone")
        self.table.heading("Observações", text="Observações")
        self.table.pack(side="left", fill="both", expand=True)

        # Barra de Scroll
        scrollbar = ttk.Scrollbar(self.frame_table, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.ver_clientes()

    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        nif = self.entry_nif.get()
        email = self.entry_email.get()
        tel = self.entry_tel.get()
        obs = self.entry_obs.get()

        campos_obrigatorios = [
            (self.entry_nome, nome),
            (self.entry_nif, nif),
            (self.entry_email, email),
            (self.entry_tel, tel)
        ]

        campos_vazios = [campo for campo, valor in campos_obrigatorios if not valor]

        if campos_vazios:
            for campo in campos_vazios:
                campo.configure(fg_color="#ffcccc")

            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
        else:
            Cliente.criar_cliente(nome, nif, email, tel, obs)
            messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
            self.limpar_campos()
            self.ver_clientes()

    def atualizar_cliente(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione um cliente para atualizar.")
            return

        id_cliente = self.table.item(selected_item)["values"][0]
        nome = self.entry_nome.get()
        nif = self.entry_nif.get()
        email = self.entry_email.get()
        tel = self.entry_tel.get()
        obs = self.entry_obs.get()

        if id_cliente and nome and nif and email and tel:
            Cliente.atualizar_cliente(id_cliente, nome, tel, nif, email, obs)
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            self.limpar_campos()
            self.ver_clientes()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")

    def deletar_cliente(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione um cliente para deletar.")
            return

        id_cliente = self.table.item(selected_item)["values"][0]

        if id_cliente:
            Cliente.deletar_cliente(id_cliente)
            messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
            self.limpar_campos()
            self.ver_clientes()
        else:
            messagebox.showerror("Erro", "Por favor, preencha o ID do cliente.")

    def ver_clientes(self):
        clientes = Cliente.buscar_todos_clientes()
        for row in self.table.get_children():
            self.table.delete(row)
        for cliente in clientes:
            self.table.insert("", "end", values=(cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]))

    def limpar_campos(self):
        self.entry_nome.delete(0, 'end')
        self.entry_nif.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_tel.delete(0, 'end')
        self.entry_obs.delete(0, 'end')

        for entry in [self.entry_nome, self.entry_nif, self.entry_email, self.entry_tel]:
            entry.configure(fg_color="#ffffff")

if __name__ == "__main__":
    app = ClientView()
    app.mainloop()
