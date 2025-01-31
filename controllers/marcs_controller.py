from models.marcsarcs import Marcacoes

class MarcsController:
    @staticmethod
    def criar_marcacao(data_marc, tipo_trabalho, veiculo, estado):
        Marcacoes.criar_marcacao(data_marc, tipo_trabalho, veiculo, estado)

    @staticmethod
    def buscar_todas_marcacoes():
        return Marcacoes.buscar_todas_marcacoes()

    @staticmethod
    def atualizar_marcacao(marcacao_id, data_marc=None, tipo_trabalho=None, veiculo=None, estado=None):
        Marcacoes.atualizar_marcacao(marcacao_id, data_marc, tipo_trabalho, veiculo, estado)

    @staticmethod
    def deletar_marcacao(marcacao_id):
        Marcacoes.deletar_marcacao(marcacao_id)