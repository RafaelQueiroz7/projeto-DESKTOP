import json
import os

# Ajusta o caminho do arquivo para a raiz do projeto: PROJETO LOCADORA/usuarios_data.json
DATABASE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'usuarios_data.json')

class GerenciadorUsuario:
    """Gerencia a persistência e a lógica de autenticação de usuários."""
    
    def __init__(self):
        # Carrega o estado no construtor
        self._usuarios = self._carregar_dados()
        
    def _carregar_dados(self) -> list:
        """Carrega a lista de usuários do arquivo JSON."""
        if not os.path.exists(DATABASE_FILE):
            return []
        try:
            with open(DATABASE_FILE, 'r') as f:
                dados = json.load(f)
                return dados.get('usuarios', [])
        except (json.JSONDecodeError, FileNotFoundError, Exception):
            print("AVISO: Erro ao carregar ou arquivo de usuários JSON corrompido.")
            return []

    def _salvar_dados(self):
        """Salva a lista atual de usuários no arquivo JSON."""
        try:
            with open(DATABASE_FILE, 'w') as f:
                json.dump({'usuarios': self._usuarios}, f, indent=4)
        except Exception as e:
            print(f"ERRO: Não foi possível salvar usuários no JSON: {e}")

    def cadastrar_usuario(self, username: str, senha: str):
        """Cadastra um novo usuário se ele não existir."""
        if any(u['username'] == username for u in self._usuarios):
            print(f"ERRO: Usuário '{username}' já existe.")
            return False
            
    
        novo_usuario = {
            'username': username,
            'senha': senha 
        }
        
        self._usuarios.append(novo_usuario)
        self._salvar_dados()
        print(f"SUCESSO: Usuário '{username}' cadastrado e salvo.")
        return True

    def autenticar_usuario(self, username: str, senha: str) -> bool:
        """Verifica se o nome de usuário e a senha coincidem."""
        
        # Busca o usuário pelo nome
        usuario = next((u for u in self._usuarios if u['username'] == username), None)
        
        if usuario and usuario['senha'] == senha:
            print(f"SUCESSO: Autenticação de '{username}' realizada.")
            return True
        else:
            print(f"FALHA: Usuário ou senha inválidos para '{username}'.")
            return False