from database.db import create_connection, close_connection

class Veiculo:
    def __init__(self, id_veiculo=None, marca=None, modelo=None, cliente_id=None, matricula=None, km=None, obs=None):
        self.id_veiculo = id_veiculo
        self.marca = marca
        self.modelo = modelo
        self.cliente_id = cliente_id
        self.matricula = matricula
        self.km = km
        self.obs = obs

    @staticmethod
    def criar_veiculo(marca, modelo, cliente_id, matricula, km, obs):
        """Cria um novo veículo no banco de dados."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                INSERT INTO Veiculo (Marca_id, Modelo_id, Cliente_id, Matricula, Km, OBS)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (marca, modelo, cliente_id, matricula, km, obs))
                connection.commit()
                print("Veículo criado com sucesso!")
            except Exception as e:
                print(f"Erro ao criar veículo: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def buscar_todos_veiculos():
        """Retorna todos os veículos cadastrados."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """
                SELECT Veiculo.Veiculo_id, Marca.Nome AS Marca, Modelo.Nome AS Modelo, Cliente.NomeCliente AS Cliente,
                       Veiculo.Matricula, Veiculo.Km, Veiculo.OBS
                FROM Veiculo
                JOIN Marca ON Veiculo.Marca_id = Marca.Marca_id
                JOIN Modelo ON Veiculo.Modelo_id = Modelo.Modelo_id
                JOIN Cliente ON Veiculo.Cliente_id = Cliente.idCliente
                """
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except Exception as e:
                print(f"Erro ao buscar veículos: {e}")
                return []
            finally:
                close_connection(connection)

    @staticmethod
    def atualizar_veiculo(id_veiculo, marca=None, modelo=None, cliente_id=None, matricula=None, km=None, obs=None):
        """Atualiza os dados de um veículo."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                UPDATE Veiculo
                SET Marca_id = %s, Modelo_id = %s, Cliente_id = %s, Matricula = %s, Km = %s, OBS = %s
                WHERE Veiculo_id = %s
                """
                cursor.execute(query, (marca, modelo, cliente_id, matricula, km, obs, id_veiculo))
                connection.commit()
                print("Veículo atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar veículo: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def deletar_veiculo(id_veiculo):
        """Remove um veículo do banco de dados."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM Veiculo WHERE Veiculo_id = %s"
                cursor.execute(query, (id_veiculo,))
                connection.commit()
                print("Veículo deletado com sucesso!")
            except Exception as e:
                print(f"Erro ao deletar veículo: {e}")
            finally:
                close_connection(connection)
    
    @staticmethod
    def totalVeiculos():
        """Total de veículos"""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM veiculo")
                total = cursor.fetchone()[0]
                return total
            except Exception as e:
                print(f"Erro ao buscar total de veículos: {e}")
                return 0
            finally:
                close_connection(connection)    

    @staticmethod
    def buscar_marcas():
        """Busca todas as marcas de veículos cadastradas."""
        connection = create_connection()
        if connection:
            try:
               cursor = connection.cursor(dictionary=True)
               cursor.execute("SELECT Marca_id, Nome FROM Marca")
               marcas = cursor.fetchall()
               print("Marcas carregadas:", marcas)  # Log para depuração
               return marcas
            except Exception as e:
               print(f"Erro ao buscar marcas: {e}")
               return []
            finally:
               close_connection(connection)
