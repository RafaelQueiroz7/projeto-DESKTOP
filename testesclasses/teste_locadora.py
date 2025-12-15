from package.locadora_app import Locadora

def workspace():
          locadora = Locadora()

          locadora.cadastrar_veiculo("ABCD1234", 50.0)
          locadora.cadastrar_cliente("12345678900", "Rafael")

          locadora.processar_aluguel("12345678900", "ABCD1234", 3)

          locadora.processar_devolucao("ABCD1234")

if __name__ == "__main__":
     
    workspace()
