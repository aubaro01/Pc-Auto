from database.db import create_connection, close_connection

class Cliente:
    def __init__(self, id_cliente=None, nome=None, tel=None, nif=None, email=None, obs=None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.tel = tel
        self.nif = nif
        self.email = email
        self.obs = obs

    @staticmethod
    def criar_cliente(nome, nif, email, tel, obs):
        """Adicionar um cliente."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO cliente (Nome_Cliente, NIF, Email_Cliente, Contacto_Cliente, obs) VALUES (%s, %s, %s, %s, %s)",
                    (nome, nif, email, tel, obs)
                )
                connection.commit()
            except Exception as e:
                print(f"Erro ao adicionar cliente: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def buscar_todos_clientes():
        """Ver tabela de clientes"""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM cliente")
                clientes = cursor.fetchall()
                return clientes
            except Exception as e:
                print(f"Erro ao buscar clientes: {e}")
                return []
            finally:
                close_connection(connection)

    @staticmethod
    def atualizar_cliente(id_cliente, nome=None, tel=None, nif=None, email=None, obs=None):
        """Atualizar um cliente."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "UPDATE cliente SET Nome_Cliente=%s, Contacto_Cliente=%s, NIF=%s, Email_Cliente=%s, obs=%s WHERE id_Cliente=%s",
                    (nome, tel, nif, email, obs, id_cliente)
                )
                connection.commit()
            except Exception as e:
                print(f"Erro ao atualizar cliente: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def deletar_cliente(id_cliente):
        """Deletar um cliente."""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM cliente WHERE id_Cliente=%s", (id_cliente,))
                connection.commit()
            except Exception as e:
                print(f"Erro ao deletar cliente: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def totalClientes():
        """Total de clientes"""
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM cliente")
                cliente = cursor.fetchone()
                return cliente[0] if cliente else 0
            except Exception as e:
                print(f"Erro ao buscar total de clientes: {e}")
                return 0
            finally:
                close_connection(connection)