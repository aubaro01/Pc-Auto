from datetime import datetime
from collections import defaultdict

class RelatorioController:
    @staticmethod
    def obter_novos_clientes_por_mes(ano=None):
        # Simulação de dados
        dados = [
            {"data": "2025-01-15"},
            {"data": "2025-02-20"},
            {"data": "2025-02-25"},
            {"data": "2025-03-10"},
            {"data": "2025-03-15"},
            {"data": "2025-04-05"},
            {"data": "2025-04-20"},
            {"data": "2025-05-10"},
            {"data": "2025-05-15"},
            {"data": "2025-06-05"},
        ]
        # Filtra os dados pelo ano, se informado
        if ano:
            dados = [d for d in dados if datetime.strptime(d["data"], "%Y-%m-%d").year == int(ano)]
        return RelatorioController._agrupar_por_mes(dados)

    @staticmethod
    def obter_novos_carros_por_mes(ano=None):
        # Simulação de dados
        dados = [
            {"data": "2025-01-10"},
            {"data": "2025-01-20"},
            {"data": "2025-02-15"},
            {"data": "2025-02-25"},
            {"data": "2025-03-05"},
            {"data": "2025-03-20"},
            {"data": "2025-04-10"},
            {"data": "2025-04-25"},
            {"data": "2025-05-05"},
            {"data": "2025-05-20"},
        ]
        if ano:
            dados = [d for d in dados if datetime.strptime(d["data"], "%Y-%m-%d").year == int(ano)]
        return RelatorioController._agrupar_por_mes(dados)

    @staticmethod
    def obter_novas_marcacoes_por_mes(ano=None):
        # Simulação de dados
        dados = [
            {"data": "2025-01-05"},
            {"data": "2025-01-15"},
            {"data": "2025-02-10"},
            {"data": "2025-02-20"},
            {"data": "2025-03-15"},
            {"data": "2025-03-25"},
            {"data": "2025-04-10"},
            {"data": "2025-04-20"},
            {"data": "2025-05-15"},
            {"data": "2025-05-25"},
        ]
        if ano:
            dados = [d for d in dados if datetime.strptime(d["data"], "%Y-%m-%d").year == int(ano)]
        return RelatorioController._agrupar_por_mes(dados)

    @staticmethod
    def _agrupar_por_mes(dados):
        resultado = defaultdict(int)
        for item in dados:
            mes = datetime.strptime(item["data"], "%Y-%m-%d").strftime("%Y-%m")
            resultado[mes] += 1
        return dict(resultado)
