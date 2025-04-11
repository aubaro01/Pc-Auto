import customtkinter as ctk
from views.auth_view import AuthView


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")





def mostrar_informacoes(veiculo):
    print(veiculo.exibir_info())

carro = Carro("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "ddd", 2019, 500)

mostrar_informacoes(carro)  
mostrar_informacoes(moto)   


if __name__ == "__main__":
    app = AuthView()
    app.mainloop()

    