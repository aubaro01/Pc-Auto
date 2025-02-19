from controllers.veiculo_controller import VeiculoController

# Criar um novo veículo
if VeiculoController.criar_veiculo(1, 2, 3, "ABC-1234", 50000, "Revisão em dia"):
    print("Veículo criado com sucesso!")
else:
    print("Erro ao criar veículo.")

# Buscar todos os veículos
veiculos = VeiculoController.buscar_todos_veiculos()
if veiculos:
    for veiculo in veiculos:
        print(veiculo)
else:
    print("Erro ao buscar veículos.")

# Atualizar um veículo
if VeiculoController.atualizar_veiculo(1, km=60000, obs="Troca de óleo realizada"):
    print("Veículo atualizado com sucesso!")
else:
    print("Erro ao atualizar veículo.")

# Deletar um veículo
if VeiculoController.deletar_veiculo(1):
    print("Veículo deletado com sucesso!")
else:
    print("Erro ao deletar veículo.")