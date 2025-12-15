import json
import os

# --- 1. GERENCIAMENTO DE PERSISTÊNCIA JSON ---
DATABASE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'locadora_data.json') 

def carregar_dados_json() -> dict:
    dados_vazios = {'clientes': [], 'veiculos': [], 'alugueis': []}
    if not os.path.exists(DATABASE_FILE):
        return dados_vazios
    try:
        with open(DATABASE_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, Exception) as e:
        print(f"AVISO: Erro ao carregar ou arquivo JSON corrompido ({e}). Iniciando com dados vazios.")
        return dados_vazios

def salvar_dados_json(dados: dict):
    try:
        with open(DATABASE_FILE, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"ERRO: Não foi possível salvar dados no JSON: {e}")

def serializar_objeto(objeto):
    if hasattr(objeto, '__dict__'):
        dados = {k.lstrip('_'): v for k, v in objeto.__dict__.items()}
        if isinstance(objeto, Aluguel):
             dados['veiculo_placa'] = objeto.get_placa_veiculo()
             dados['cliente_cpf'] = objeto.get_cpf_cliente()
             del dados['veiculo_alugado']
             del dados['cliente_responsavel']
        return dados
    raise TypeError(f"Objeto do tipo {type(objeto)} não serializável")

def desserializar_objeto(dados: dict, classe, **kwargs):
    if classe == Aluguel:
        veiculo_obj = kwargs.get('veiculo')
        cliente_obj = kwargs.get('cliente')
        dias = dados.get('dias')
        return Aluguel(veiculo_obj, cliente_obj, dias)

    instance = classe.__new__(classe)
    for key, value in dados.items():
        setattr(instance, f'_{key}', value)
    return instance

# --- 2. CLASSES MODELO ---

class Veiculo:
    def __init__(self, placa: str, valorDiaria: float):
        self._placa = placa
        self._valorDiaria = valorDiaria
        self._disponivel = True

    def alternar_disponibilidade(self):
        self._disponivel = not self._disponivel
        
    def get_placa(self) -> str:
        return self._placa

    def get_valorDiaria(self) -> float:
        return self._valorDiaria

    def esta_disponivel(self) -> bool:
        return self._disponivel

class Cliente:
    def __init__(self, cpf: str, nome: str):
        self._cpf = cpf
        self._nome = nome

    def verificarIdentidade(self):
        return f"Cliente: {self._nome} (CPF: {self._cpf})"

    def get_cpf(self) -> str:
        return self._cpf

    def get_nome(self) -> str:
        return self._nome

class Aluguel:
    def __init__(self, veiculo, cliente, dias: int):
        self._veiculo_alugado = veiculo
        self._cliente_responsavel = cliente
        self._dias = dias
    
    def calcular_custo(self) -> float:
        valorDiaria = self._veiculo_alugado.get_valorDiaria()
        custo_total = valorDiaria * self._dias
        return custo_total

    def get_placa_veiculo(self) -> str:
        return self._veiculo_alugado.get_placa()

    def get_cpf_cliente(self) -> str:
        return self._cliente_responsavel.get_cpf()

    def get_dias_previstos(self) -> int:
        return self._dias


# --- 3. CLASSE LOCADORA REFATORADA ---

class Locadora:
    
    NOME_DA_LOCADORA = "Locadora Queiroz"
    
    def __init__(self):
        self._frota = []
        self._clientes = []
        self._alugueis_ativos = []
        self.carregar_estado()

    def carregar_estado(self):
        dados = carregar_dados_json()
        
        self._clientes = [desserializar_objeto(d, Cliente) for d in dados['clientes'] if d]
        self._frota = [desserializar_objeto(d, Veiculo) for d in dados['veiculos'] if d]

        for aluguel_data in dados['alugueis']:
            placa = aluguel_data.get('veiculo_placa')
            cpf = aluguel_data.get('cliente_cpf')
            
            veiculo = next((v for v in self._frota if v.get_placa() == placa), None)
            cliente = next((c for c in self._clientes if c.get_cpf() == cpf), None)
            
            if veiculo and cliente:
                novo_aluguel = desserializar_objeto(aluguel_data, Aluguel, veiculo=veiculo, cliente=cliente)
                self._alugueis_ativos.append(novo_aluguel)
            else:
                print(f"AVISO: Aluguel no JSON inconsistente (Placa: {placa}, CPF: {cpf}). Ignorado.")
        
        print(f"SUCESSO: Estado da Locadora '{self.NOME_DA_LOCADORA}' carregado do JSON.")

    def _salvar_estado(self):
        dados = {
            'clientes': [serializar_objeto(c) for c in self._clientes],
            'veiculos': [serializar_objeto(v) for v in self._frota],
            'alugueis': [serializar_objeto(a) for a in self._alugueis_ativos]
        }
        salvar_dados_json(dados)

    def get_nome(self) -> str:
        return self.NOME_DA_LOCADORA
    
    # --- MÉTODOS REQUERIDOS PELO DASHBOARD ---
    
    def get_clientes(self) -> dict:
        """Retorna um dicionário de clientes no formato {cpf: nome}."""
        return {c.get_cpf(): c.get_nome() for c in self._clientes}

    def consultar_frota_alugada(self) -> list:
        """Retorna uma lista de placas de veículos que estão atualmente alugados (indisponíveis)."""
        # Pega as placas diretamente dos aluguéis ativos para maior precisão
        return [a.get_placa_veiculo() for a in self._alugueis_ativos]

    # --- MÉTODOS DE NEGÓCIO (Modificados para retornar strings) ---
    
    
    def cadastrar_cliente(self, cpf: str, nome: str):
        if any(c.get_cpf() == cpf for c in self._clientes):
            return f"ERRO: Cliente com CPF {cpf} já cadastrado."
        
        novo_cliente = Cliente(cpf, nome)
        self._clientes.append(novo_cliente)
        self._salvar_estado() 
        return f"SUCESSO: Cliente {nome} cadastrado e salvo no JSON."

    def cadastrar_veiculo(self , placa: str, valorDiaria: float):
        if any(v.get_placa() == placa for v in self._frota):
            return f"ERRO: Veículo {placa} já cadastrado."

        novo_veiculo = Veiculo(placa, valorDiaria)
        self._frota.append(novo_veiculo)
        self._salvar_estado()
        return f"SUCESSO: Veículo de placa: {placa} (R$ {valorDiaria:.2f} por dia) adicionado e salvo no JSON."

    def processar_aluguel(self, cpf: str, placa: str, dias: int):
        cliente = next((c for c in self._clientes if c.get_cpf() == cpf), None)
        veiculo = next((v for v in self._frota if v.get_placa() == placa), None)
        
        if not cliente:
            return f"FALHA NO ALUGUEL: Cliente com CPF {cpf} não encontrado."
        if not veiculo:
            return f"FALHA NO ALUGUEL: Veículo de placa {placa} não encontrado."
        if not veiculo.esta_disponivel():
            return f"FALHA NO ALUGUEL: Veiculo de placa {placa} já está alugado."

        veiculo.alternar_disponibilidade()
        novo_aluguel = Aluguel(veiculo, cliente, dias)
        self._alugueis_ativos.append(novo_aluguel)
        self._salvar_estado() 
        
        custo = novo_aluguel.calcular_custo()
        return f"SUCESSO: Aluguel REALIZADO para {cliente.get_nome()} (Veículo: {placa}). Custo R$ {custo:.2f}."

    def processar_devolucao(self, placa:str):
        aluguel_ativo = next((a for a in self._alugueis_ativos if a.get_placa_veiculo() == placa), None)
        if not aluguel_ativo:
            return f"FALHA NA DEVOLUÇÃO: Não há aluguel ativo para a placa {placa}."

        custo_final = aluguel_ativo.calcular_custo()
        veiculo = aluguel_ativo._veiculo_alugado
        veiculo.alternar_disponibilidade()
        self._alugueis_ativos.remove(aluguel_ativo)
        
        self._salvar_estado()
        
        return f"SUCESSO: Devolução CONCLUÍDA. Veículo {placa} devolvido. VALOR A PAGAR: R$ {custo_final:.2f}."

    def consultar_frota_disponivel_lista(self):
        disponiveis = [v for v in self._frota if v.esta_disponivel()]
        return [v.get_placa() for v in disponiveis] # Retorna apenas a lista de placas

    def get_frota(self):
        return self._frota
    

    def get_clientes_list(self):
      """Retorna a lista de objetos Cliente."""
      return self._clientes
    
    def get_veiculos_disponiveis_list(self):
      """Retorna uma lista de objetos Veiculo disponíveis."""
      return [v for v in self._frota if v.esta_disponivel()]