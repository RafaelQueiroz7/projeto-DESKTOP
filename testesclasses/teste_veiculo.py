from package.locadora_app import Veiculo

def workspace():
       carro1 = Veiculo("ABCD1234", 50.00)
       print(f"Veiculo criado: {carro1.get_placa()}.")

       print(f"Status inicial: Disponível: {carro1.esta_disponivel()}")
       
       diaria = carro1.get_valorDiaria()
       print(f"valor da diária : R${diaria:.2f}.")

if __name__ == "__main__":
    workspace()
