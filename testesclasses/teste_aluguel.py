from package.locadora_app import Aluguel
from package.locadora_app import Veiculo
from package.locadora_app import Cliente

def workspace():
    vteste = Veiculo("RAQ777", 100.00)
    cteste = Cliente("1023546", "João")
    dias = 4

    aluguel_transacao = Aluguel(vteste, cteste, dias)
    print("objeto Aluguel criado.")
    print(f"Veículo associado: {aluguel_transacao.get_placa_veiculo()}")

    custo_calculado = aluguel_transacao.calcular_custo()
    print(f"Custo total calculado: R${custo_calculado:.2f}")

if __name__ == "__main__":
    workspace()
