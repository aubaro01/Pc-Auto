import customtkinter as ctk
from tkinter import messagebox
from controllers.auth_controller import AuthController
from views.main_app import MainApp

# Melhorar design, janelas de texto 
#Retirar a mensagem de login 

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AuthView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pc Auto - Autenticação")
        self.geometry("500x400")
        self.resizable(False, False) # Não permitir redimensionamento

        # icon
       # try:
           # self.iconbitmap("assets/icon.ico")  
      #  except Exception as e:
          #  print(f"Erro ao carregar o ícone: {e}")

        self.auth_controller = AuthController()

        self.label_title = ctk.CTkLabel(self, text="Login", font=("Arial", 26, "bold"))
        self.label_title.pack(pady=20)

        self.label_subtitle = ctk.CTkLabel(self, text="Pc Auto", font=("Arial", 14, "italic"), text_color="gray")
        self.label_subtitle.pack(pady=5)

        self.entry_username_frame = ctk.CTkFrame(self, corner_radius=8)
        self.entry_username_frame.pack(pady=10)
        self.icon_user = ctk.CTkLabel(self.entry_username_frame, text="\uD83D\uDC64")  
        self.icon_user.pack(side="left", padx=5)
        self.entry_username = ctk.CTkEntry(self.entry_username_frame, placeholder_text="Nome de usuário", width=260)
        self.entry_username.pack(side="right", padx=5)


        self.label_error_username = ctk.CTkLabel(self, text="", text_color="red")
        self.label_error_username.pack()

        self.frame_password = ctk.CTkFrame(self, corner_radius=8)
        self.frame_password.pack(pady=10)

        self.entry_password = ctk.CTkEntry(self.frame_password, placeholder_text="Senha", show="*", width=260)
        self.entry_password.pack(side="left", padx=(10, 0), pady=5)

        self.show_password = False
        self.button_show_password = ctk.CTkButton(
            self.frame_password, text="🔒", width=40, command=self.toggle_password_visibility, corner_radius=8
        )
        self.button_show_password.pack(side="right", padx=10)

        self.label_error_password = ctk.CTkLabel(self, text="", text_color="red")
        self.label_error_password.pack()

        self.button_login = ctk.CTkButton(self, text="Login", command=self.login, state="disabled", width=200, corner_radius=8)
        self.button_login.pack(pady=20)

        self.entry_username.bind("<KeyRelease>", self.check_fields)
        self.entry_password.bind("<KeyRelease>", self.check_fields)

        self.button_login.bind("<Enter>", lambda e: self.button_login.configure(fg_color="dodgerblue"))
        self.button_login.bind("<Leave>", lambda e: self.button_login.configure(fg_color="lightblue"))


    def toggle_password_visibility(self):
        """Alterna a visibilidade da senha."""
        if self.show_password:
            self.entry_password.configure(show='*')
            self.button_show_password.configure(text="🔒")  
        else:
            self.entry_password.configure(show='')
            self.button_show_password.configure(text="🔐") 
        self.show_password = not self.show_password

    def check_fields(self, event=None):
        """Verifica se os campos foram preenchidos corretamente."""
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username:
            self.label_error_username.configure(text="Por favor, preencha o campo de nome de usuário.")
        else:
            self.label_error_username.configure(text="")

        if not password:
            self.label_error_password.configure(text="Por favor, preencha o campo de senha.")
        else:
            self.label_error_password.configure(text="")

        if username and password:
            self.button_login.configure(state="normal")
            self.button_login.configure(fg_color="lightblue")
        else:
            self.button_login.configure(state="disabled")
            self.button_login.configure(fg_color="gray")

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
