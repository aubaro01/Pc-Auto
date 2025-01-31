import customtkinter as ctk
from tkinter import messagebox
from controllers.auth_controller import AuthController
from views.main_app import MainApp  # Importação da MainApp

# Configurações globais do tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AuthView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pc_Auto - Autenticação")
        self.geometry("500x400")
        self.resizable(False, False)

        # Adicionar ícone à janela
        try:
            self.iconbitmap("assets/icon.ico")  # Certifique-se de que o arquivo .ico exista
        except Exception as e:
            print(f"Erro ao carregar o ícone: {e}")

        self.auth_controller = AuthController()

        # Título principal
        self.label_title = ctk.CTkLabel(self, text="Login", font=("Arial", 24, "bold"))
        self.label_title.pack(pady=20)

        # Subtítulo
        self.label_subtitle = ctk.CTkLabel(self, text="Pc Auto Dash", font=("Arial", 16))
        self.label_subtitle.pack(pady=5)

        # Campo de username
        self.entry_username = ctk.CTkEntry(self, placeholder_text="Username", width=300)
        self.entry_username.pack(pady=10)

        self.label_error_username = ctk.CTkLabel(self, text="", text_color="red")
        self.label_error_username.pack()

        # Frame para o campo de senha e botão de visibilidade
        self.frame_password = ctk.CTkFrame(self, corner_radius=8)
        self.frame_password.pack(pady=10)

        self.entry_password = ctk.CTkEntry(self.frame_password, placeholder_text="Senha", show="*", width=260)
        self.entry_password.pack(side="left", padx=(10, 0), pady=5)

        self.show_password = False
        self.button_show_password = ctk.CTkButton(self.frame_password, text="👁", width=40, command=self.toggle_password_visibility)
        self.button_show_password.pack(side="right", padx=10)

        self.label_error_password = ctk.CTkLabel(self, text="", text_color="red")
        self.label_error_password.pack()

        # Botão de login
        self.button_login = ctk.CTkButton(self, text="Login", command=self.login, state="disabled", width=200)
        self.button_login.pack(pady=20)

        # Bind para verificar campos ao digitar
        self.entry_username.bind("<KeyRelease>", self.check_fields)
        self.entry_password.bind("<KeyRelease>", self.check_fields)

    def toggle_password_visibility(self):
        """Alterna a visibilidade da senha."""
        if self.show_password:
            self.entry_password.configure(show='*')
            self.button_show_password.configure(text="👁")
        else:
            self.entry_password.configure(show='')
            self.button_show_password.configure(text="👁‍🗨")
        self.show_password = not self.show_password

    def check_fields(self, event=None):
        """Verifica se os campos foram preenchidos corretamente."""
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username:
            self.label_error_username.configure(text="Por favor, preencha o campo de username.")
        else:
            self.label_error_username.configure(text="")

        if not password:
            self.label_error_password.configure(text="Por favor, preencha o campo de senha.")
        else:
            self.label_error_password.configure(text="")

        if username and password:
            self.button_login.configure(state="normal")
        else:
            self.button_login.configure(state="disabled")

    def login(self):
        """Lógica de autenticação."""
        username = self.entry_username.get()
        password = self.entry_password.get()

        success, message = self.auth_controller.login(username, password)
        if success:
            messagebox.showinfo("Sucesso", message)
            self.destroy()
            MainApp().mainloop()
        else:
            messagebox.showerror("Erro", message)

if __name__ == "__main__":
    app = AuthView()
    app.mainloop()