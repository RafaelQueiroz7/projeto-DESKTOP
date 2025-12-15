from package.locadora_app import Cliente

def workspace():
    cliente1 = Cliente("12345678900", "Rafael")
    print(f"Cliente criado: {cliente1.get_nome()}")

    identidade = cliente1.verificarIdentidade()
    print(f"Identidade completa: {identidade}")

    print(f"CPF: {cliente1.get_cpf()}")

if __name__ == "__main__":
    workspace()
