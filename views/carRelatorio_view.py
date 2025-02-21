import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controllers.relatorio_controller import RelatorioController
import threading

    # Constantes para cores e estilos
BACKGROUND_COLOR = "#2e2e2e"
BUTTON_COLOR = "#1f6aa5"
BUTTON_HOVER_COLOR = "#155a8c"
TEXT_COLOR = "white"
FONT_STYLE = ("Arial", 16)
GRAPH_COLORS = ["blue", "green", "red"]

class CarRelatorioView(ctk.CTk):
        def __init__(self):
            super().__init__()

            self.title("Relatório de Carros")
            self.geometry("1200x800")
            self.resizable(True, True)
            self.configure(bg=BACKGROUND_COLOR)

            # Título Principal
            self.label_title = ctk.CTkLabel(
                self,
                text="Relatório de Carros",
                font=("Arial", 26, "bold"),
                fg_color=BUTTON_COLOR,
                text_color=TEXT_COLOR
            )
            self.label_title.pack(fill="x", pady=(10, 20))

            # Frame para os gráficos
            self.graph_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)
            self.graph_frame.pack(pady=10, padx=20, fill="both", expand=True)

            # Botão para gerar gráficos
            self.generate_button = ctk.CTkButton(
                self,
                text="Gerar Gráficos",
                fg_color=BUTTON_COLOR,
                hover_color=BUTTON_HOVER_COLOR,
                text_color=TEXT_COLOR,
                command=self.threaded_gerar_graficos
            )
            self.generate_button.pack(pady=20)

            # Referência para o canvas (opcional para futuras atualizações)
            self.canvas = None

        def threaded_gerar_graficos(self):
            """Inicia a geração de gráficos em uma thread separada."""
            self.generate_button.configure(state="disabled", text="Gerando...")
            threading.Thread(target=self.gerar_graficos, daemon=True).start()

        def gerar_graficos(self):
            """Gera e exibe os gráficos com base nos dados do controlador."""
            try:
                # Obter dados do controlador
                dados_clientes = RelatorioController.obter_novos_clientes_por_mes()
                dados_carros = RelatorioController.obter_novos_carros_por_mes()
                dados_marcacoes = RelatorioController.obter_novas_marcacoes_por_mes()

                # Verificar se os dados são válidos
                if not all([dados_clientes, dados_carros, dados_marcacoes]):
                    raise ValueError("Dados inválidos retornados pelo controlador.")

                # Limpar o frame dos gráficos
                for widget in self.graph_frame.winfo_children():
                    widget.destroy()

                # Aplicar um estilo mais moderno
                plt.style.use('seaborn-darkgrid')

                # Criar figura e eixos com layout ajustado
                fig, axs = plt.subplots(3, 1, figsize=(12, 18), constrained_layout=True)

                # Criar os gráficos
                self._plot_graph(axs[0], dados_clientes, 'Novos Clientes por Mês', 'Número de Clientes', GRAPH_COLORS[0])
                self._plot_graph(axs[1], dados_carros, 'Novos Carros por Mês', 'Número de Carros', GRAPH_COLORS[1])
                self._plot_graph(axs[2], dados_marcacoes, 'Novas Marcações por Mês', 'Número de Marcações', GRAPH_COLORS[2])

                # Adicionar o canvas com os gráficos ao frame
                if self.canvas:
                    self.canvas.get_tk_widget().destroy()  # Destruir o canvas anterior
                self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
                self.canvas.draw()
                self.canvas.get_tk_widget().pack(fill="both", expand=True)

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao gerar gráficos: {e}")
            finally:
                # Habilitar novamente o botão
                self.generate_button.configure(state="normal", text="Gerar Gráficos")
                plt.close()  # Liberar memória

        def _plot_graph(self, ax, data, title, ylabel, color):
            """Cria um gráfico de barras com os dados fornecidos."""
            meses = list(data.keys())
            contagens = list(data.values())

            # Cria gráfico de barras
            bars = ax.bar(meses, contagens, color=color, alpha=0.8)
            ax.set_title(title, fontsize=16, fontweight='bold')
            ax.set_xlabel('Mês', fontsize=14)
            ax.set_ylabel(ylabel, fontsize=14)
            ax.tick_params(axis='x', rotation=45)

            # Adiciona rótulos com os valores acima de cada barra
            for bar in bars:
                altura = bar.get_height()
                ax.annotate(f'{altura}',
                            xy=(bar.get_x() + bar.get_width() / 2, altura),
                            xytext=(0, 3),  # deslocamento vertical em pontos
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=10)
            ax.grid(True, linestyle='--', alpha=0.7)

if __name__ == "__main__":
    app = CarRelatorioView()
    app.mainloop()