import bcrypt
from models.db import create_connection, close_connection

def get_user_by_username(username):
    """Obtém os dados do usuário pelo nome de usuário."""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM admin WHERE Log_admin = %s', (username,))
            user = cursor.fetchone()
            return user
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return None
        finally:
            close_connection(conn)
    else:
        print("Erro ao conectar ao banco de dados.")
    return None

def verify_user_password(user, password):
    """
    Verifica a senha do usuário comparando com o hash armazenado no banco de dados.

    Args:
        user (dict): Dicionário com os dados do usuário.
        password (str): Senha fornecida pelo usuário.

    Returns:
        bool: True se a senha for válida, False caso contrário.
    """
    if user is None:
        print("Usuário não encontrado.")
        return False

    try:
        # Recupera o hash da senha armazenada
        stored_password = user['Pass_admin']
        # Verifica a senha fornecida
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            return True
        print("Senha incorreta.")
        return False
    except Exception as e:
        print(f"Erro ao verificar a senha: {e}")
        return False

def hash_password(password):
    """
    Gera um hash seguro para uma senha.

    Args:
        password (str): Senha em texto simples.

    Returns:
        str: Hash seguro da senha.
    """
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')
    except Exception as e:
        print(f"Erro ao gerar o hash da senha: {e}")
        return None
