import customtkinter as ctk
from views.auth_view import AuthView


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    app = AuthView()
    app.mainloop()