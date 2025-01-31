from database.db import create_connection, close_connection

class Marcacoes:
    def __init__(self, marcacao_id=None, data_marc=None, tipo_trabalho_id=None, veiculo_id=None, estado=None):
        self.marcacao_id = marcacao_id
        self.data_marc = data_marc
        self.tipo_trabalho_id = tipo_trabalho_id
        self.veiculo_id = veiculo_id
        self.estado = estado

    @staticmethod
    def criar_marcacao(data_marc, tipo_trabalho_id, veiculo_id, estado):
        """Cria uma nova marcação no banco de dados."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                INSERT INTO Marcacoes (Data_marc, Tipo_trabalho_id, Veiculo_id, Estado)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (data_marc, tipo_trabalho_id, veiculo_id, estado))
                connection.commit()
                print("Marcação criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar marcação: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def buscar_todas_marcacoes():
        """Retorna todas as marcações cadastradas."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                SELECT Marcacoes.Marcacao_id, Marcacoes.Data_marc, Tipo_trabalho.nome AS Tipo_Trabalho,
                       Veiculo.Matricula AS Veiculo, Cliente.NomeCliente AS Cliente, Estado_Marc.Estado AS Estado
                FROM Marcacoes
                JOIN Veiculo ON Marcacoes.Veiculo_id = Veiculo.Veiculo_id
                JOIN Cliente ON Veiculo.Cliente_id = Cliente.idCliente
                JOIN Tipo_trabalho ON Marcacoes.Tipo_trabalho_id = Tipo_trabalho.tipoTrabalho_id
                JOIN Estado_Marc ON Marcacoes.Estado = Estado_Marc.Estado_pk
                """
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except Exception as e:
                print(f"Erro ao buscar marcações: {e}")
                return []
            finally:
                close_connection(connection)

    @staticmethod
    def buscar_tipos_trabalho():
        """Retorna todos os tipos de trabalho cadastrados."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT id_TipoMarc, Marcacao FROM tipomarcacao"
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except Exception as e:
                print(f"Erro ao buscar tipos de trabalho: {e}")
                return []
            finally:
                close_connection(connection)

    @staticmethod
    def buscar_estados():
        """Retorna todos os estados cadastrados."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT Estado FROM marcacao"
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except Exception as e:
                print(f"Erro ao buscar estados: {e}")
                return []
            finally:
                close_connection(connection)

    @staticmethod
    def atualizar_marcacao(marcacao_id, data_marc=None, tipo_trabalho_id=None, veiculo_id=None, estado=None):
        """Atualiza os dados de uma marcação."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                UPDATE Marcacoes
                SET Data_marc = %s, Tipo_trabalho_id = %s, Veiculo_id = %s, Estado = %s
                WHERE Marcacao_id = %s
                """
                cursor.execute(query, (data_marc, tipo_trabalho_id, veiculo_id, estado, marcacao_id))
                connection.commit()
                print("Marcação atualizada com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar marcação: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def deletar_marcacao(marcacao_id):
        """Remove uma marcação do banco de dados."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM Marcacoes WHERE Marcacao_id = %s"
                cursor.execute(query, (marcacao_id,))
                connection.commit()
                print("Marcação deletada com sucesso!")
            except Exception as e:
                print(f"Erro ao deletar marcação: {e}")
            finally:
                close_connection(connection)