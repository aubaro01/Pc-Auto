from models.cars import Veiculo

def criar_veiculo(marca, modelo, cliente_id, matricula, km, obs):
    """Cria um novo veículo."""
    Veiculo.criar_veiculo(marca, modelo, cliente_id, matricula, km, obs)

def buscar_todos_veiculos():
    """Busca todos os veículos cadastrados."""
    return Veiculo.buscar_todos_veiculos()

def atualizar_veiculo(id_veiculo, marca=None, modelo=None, cliente_id=None, matricula=None, km=None, obs=None):
    """Atualiza os dados de um veículo."""
    Veiculo.atualizar_veiculo(id_veiculo, marca, modelo, cliente_id, matricula, km, obs)

def deletar_veiculo(id_veiculo):
    """Deleta um veículo."""
    Veiculo.deletar_veiculo(id_veiculo)