from package.locadora_app import Veiculo
from package.locadora_app import Cliente
from package.locadora_app import Aluguel
from package.locadora_app import Locadora

def exibir_menu():
    """Exibe as opções do menu principal."""
    print("\n" + "="*40)
    print(f"BEM-VINDO(A) À {LOCADORA.get_nome()}".center(40))
    print("="*40)
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Veículo")
    print("3. Realizar Aluguel")
    print("4. Devolver Veículo")
    print("5. Consultar Frota Disponível")
    print("6. Sair do Sistema")
    print("-" * 40)


def ler_opcao():
    """Lê a opção do usuário e garante que é um número válido."""
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("Opção inválida. Digite um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def ler_opcao():
    """Lê a opção do usuário e garante que é um número válido."""
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("Opção inválida. Digite um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# ----------------------------------------------------------------------
# FUNÇÕES DE EXECUÇÃO DOS CASOS DE USO
# ----------------------------------------------------------------------

def executar_cadastro_cliente():
    print("\n--- Cadastro de Cliente ---")
    cpf = input("CPF (apenas números): ")
    nome = input("Nome do Cliente: ")
    # A Locadora fará a validação de unicidade
    LOCADORA.cadastrar_cliente(cpf, nome)

def executar_cadastro_veiculo():
    print("\n--- Cadastro de Veículo ---")
    placa = input("Placa: ")
    
    while True:
        try:
            valor_diaria = float(input("Valor da Diária (R$): "))
            if valor_diaria > 0:
                break
            else:
                print("O valor da diária deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
            
    # A Locadora criará e adicionará o Veiculo
    LOCADORA.cadastrar_veiculo(placa, valor_diaria)
    
def executar_realizar_aluguel():
    print("\n--- Realizar Aluguel ---")
    cpf = input("CPF do Cliente: ")
    placa = input("Placa do Veículo: ")
    
    while True:
        try:
            dias = int(input("Dias Previstos de Aluguel: "))
            if dias > 0:
                break
            else:
                print("O número de dias deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    # A Locadora orquestra a transação e muda o status do veículo
    LOCADORA.processar_aluguel(cpf, placa, dias)

def executar_devolver_veiculo():
    print("\n--- Devolução de Veículo ---")
    placa = input("Placa do Veículo a ser devolvido: ")
    
    # A Locadora processa a devolução, calcula o custo e libera o veículo
    LOCADORA.processar_devolucao(placa)

def executar_consultar_frota():
    print("\n--- Consulta de Frota Disponível ---")
    LOCADORA.consultar_frota_disponivel()
    
# ----------------------------------------------------------------------
# FUNÇÃO PRINCIPAL DE CONTROLE (O Loop do Sistema)
# ----------------------------------------------------------------------

def main():
    """Loop principal do sistema de locadora."""
    
    # Inicialização do Banco de Dados / Estado (POO)
    # A variável global LOCADORA é a ÚNICA instância de gerenciamento (Singleton implícita)
    
    global LOCADORA
    LOCADORA = Locadora("Locadora Queiroz")

    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == 1:
            executar_cadastro_cliente()
        elif opcao == 2:
            executar_cadastro_veiculo()
        elif opcao == 3:
            executar_realizar_aluguel()
        elif opcao == 4:
            executar_devolver_veiculo()
        elif opcao == 5:
            executar_consultar_frota()
        elif opcao == 6:
            print("\nObrigado por usar o sistema! Encerrando...")
            break

# ----------------------------------------------------------------------
# PONTO DE ENTRADA DO PROGRAMA
# ----------------------------------------------------------------------
if __name__ == "__main__":
    main