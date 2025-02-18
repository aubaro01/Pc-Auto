from models.admin import get_user_by_username, verify_user_password

class AuthController:
    def __init__(self):
        pass

    def login(self, username, password):
        if not username or not password:
            return False, "Os campos de username e senha devem ser preenchidos."

        try:
            user = get_user_by_username(username)
            if user:
                if verify_user_password(user, password):
                    return True, "Login realizado com sucesso!"
                else:
                    return False, "Senha incorreta. Tente novamente."
            else:
                return False, "Usuário não encontrado. Tente novamente."
        except Exception as e:
            print(f"Erro no processo de login: {e}")
            return False, "Erro no processo de login. Tente novamente."