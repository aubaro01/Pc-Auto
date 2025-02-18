from models.admin import get_user_by_username, verify_user_password
import logging

class AuthController:
    def __init__(self):
        # Configuração do logger
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def login(self, username, password, show_success_message=False):
        if not username or not password:
            return False, "Os campos de username e senha devem ser preenchidos."

        try:
            user = get_user_by_username(username)
            if user:
                if verify_user_password(user, password):
                    if show_success_message:
                        return True, "Login realizado com sucesso!"
                    else:
                        return True, None
                else:
                    return False, "Senha incorreta. Tente novamente."
            else:
                return False, "Usuário não encontrado. Tente novamente."
        except Exception as e:
            self.logger.error(f"Erro no processo de login: {e}")
            return False, "Erro no processo de login. Tente novamente."

