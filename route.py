# main.py (Corrigido)

from bottle import route, run, template, static_file, request, redirect, TEMPLATE_PATH, default_app, response 
from package.locadora_app import Locadora 
from package.seguranca_app import GerenciadorUsuario 
import os

# --- Configuração de Caminhos ---

TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views'))
STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# --- Inicialização da Aplicação POO ---

LOCADORA = Locadora() 
USUARIOS = GerenciadorUsuario()


# --- Funções de Segurança ---

def checar_login(callback):
    def wrapper(*args, **kwargs):
        if request.get_cookie("logged_user"): 
            return callback(*args, **kwargs)
        else:
            return redirect('/login') 
    return wrapper

# --- Rotas ---

@route('/')
def home_page():
    return template('home')

@route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.forms.get('username')
        senha = request.forms.get('senha')
        
        if USUARIOS.autenticar_usuario(username, senha):
            response.set_cookie("logged_user", username, path='/')
            return redirect('/dashboard') 
        else:
            return template('login', error="Usuário ou senha inválidos.")
    
    return template('login', error=None)

@route('/logout')
def logout():
    response.set_cookie("logged_user", "", expires=0)
    return redirect('/')

@route('/cadastrar', method=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        username = request.forms.get('username')
        senha = request.forms.get('senha')
        
        if not username or not senha:
            return template('cadastro', error="Preencha todos os campos.")
        
        if USUARIOS.cadastrar_usuario(username, senha):
            return redirect('/login?success=true')
        else:
            return template('cadastro', error="Nome de usuário já existe ou inválido.")
            
    success_message = True if request.query.get('success') == 'true' else False
    
    return template('cadastro', error=None, success=success_message)

# ------------------------------------------------------------------
# --- ROTAS OPERAÇÕES ---------------------
# ------------------------------------------------------------------

@route('/dashboard') 
@checar_login 
def dashboard():
    """Painel principal que agora funciona como menu de navegação."""
    
    # Trata mensagens de feedback (necessário para receber o resultado dos POSTs)
    mensagem = request.query.get('msg')
    status = request.query.get('status') 

    # A rota só precisa do nome da locadora e das mensagens de status.
    return template('index', 
                    nome_locadora=LOCADORA.get_nome(), 
                    mensagem=mensagem,
                    status=status)


# --- ROTAS GET PARA FORMULÁRIOS SEPARADOS ---

@route('/cadastro/cliente')
@checar_login
def get_cadastro_cliente():
    """Exibe o formulário para cadastro de cliente."""
    return template('cadastro_cliente', nome_locadora=LOCADORA.get_nome())

@route('/cadastro/veiculo')
@checar_login
def get_cadastro_veiculo():
    """Exibe o formulário para cadastro de veículo."""
    return template('cadastro_veiculo', nome_locadora=LOCADORA.get_nome())

# main.py (Rota GET para aluguel)

# main.py (Rota GET para aluguel)

@route('/transacao/aluguel')
@checar_login
def get_processar_aluguel():
    try:
        # 1. Carrega os dados necessários para o formulário
        clientes = LOCADORA.get_clientes_list()  # Usa a lista de objetos Cliente
        veiculos_disponiveis = LOCADORA.get_veiculos_disponiveis_list() # Usa a lista de objetos Veiculo
        
        # 2. Renderiza o template com os dados
        return template('processar_aluguel',
                        nome_locadora=LOCADORA.get_nome(),
                        clientes=clientes,
                        veiculos_disponiveis=veiculos_disponiveis)
                        
    except Exception as e:
        return redirect(f'/dashboard?msg=ERRO ao carregar dados para aluguel: {e}&status=error')
    
@route('/transacao/devolucao')
@checar_login
def get_processar_devolucao():
    """Exibe o formulário para processar devolução."""
    # Precisa dos dados dos veículos alugados
    veiculos_alugados = LOCADORA.consultar_frota_alugada()
    
    return template('processar_devolucao', 
                    nome_locadora=LOCADORA.get_nome(),
                    veiculos_alugados=veiculos_alugados)



#----------ROTAS POST------------

@route('/cadastrar_cliente_post', method='POST')
@checar_login
def cadastrar_cliente_post():
    nome = request.forms.get('nome')
    cpf = request.forms.get('cpf')
    
    try:
        resultado = LOCADORA.cadastrar_cliente(cpf, nome)
        
        # 1. Verifica se houve sucesso (Case-Insensitive)
        if "sucesso" in resultado.lower().strip():
            # Sucesso: Redireciona para o Menu Principal com a mensagem
            return redirect(f'/dashboard?msg={resultado}&status=success')
        else:
            # Erro de Duplicidade: Redireciona de volta para a página do formulário
            # Sem passar a mensagem de erro na URL.
            print(f"ERRO DE VALIDAÇÃO (Cliente): {resultado}") # Opcional: manter print para debug
            return redirect('/cadastro/cliente') 
            
    except Exception as e:
        print(f"ERRO EXCEPCIONAL (Cliente): {e}") # Opcional: manter print para debug
        return redirect('/cadastro/cliente')

@route('/cadastrar_veiculo_post', method='POST')
@checar_login
def cadastrar_veiculo_post():
    placa = request.forms.get('placa')
    try:
        valor_diaria = float(request.forms.get('valor_diaria'))
        
        resultado = LOCADORA.cadastrar_veiculo(placa, valor_diaria)
        
        # 1. Verifica se houve sucesso (Case-Insensitive)
        if "sucesso" in resultado.lower().strip():
            # Sucesso: Redireciona para o Menu Principal com a mensagem
            return redirect(f'/dashboard?msg={resultado}&status=success')
        else:
            # Erro de Duplicidade: Redireciona de volta para a página do formulário
            print(f"ERRO DE VALIDAÇÃO (Veículo): {resultado}") # Opcional: manter print para debug
            return redirect('/cadastro/veiculo')
            
    except ValueError:
        # Erro: Valor da diária inválido (tente cadastrar "abc" no campo)
        print("ERRO DE VALIDAÇÃO (Veículo): Valor da diária inválido.")
        return redirect('/cadastro/veiculo')
        
    except Exception as e:
        print(f"ERRO EXCEPCIONAL (Veículo): {e}") # Opcional: manter print para debug
        return redirect('/cadastro/veiculo')


# main.py (Verifique ou ajuste sua rota processar_aluguel_post)

@route('/processar_aluguel_post', method='POST')
@checar_login
def processar_aluguel_post():
    cpf_cliente = request.forms.get('cpf_cliente')
    placa_veiculo = request.forms.get('placa_veiculo')
    
    try:
        dias = int(request.forms.get('dias'))
        
        # CHAMA A LÓGICA DE NEGÓCIO
        resultado = LOCADORA.processar_aluguel(cpf_cliente, placa_veiculo, dias)
        
        # Verifica se houve sucesso (Case-Insensitive)
        if "sucesso" in resultado.lower().strip():
            # Sucesso: Redireciona para o Menu Principal com a mensagem
            return redirect(f'/dashboard?msg={resultado}&status=success')
        else:
            # Erro de Validação: Redireciona de volta para a página do formulário
            print(f"ERRO DE VALIDAÇÃO (Aluguel): {resultado}") # Opcional: manter print para debug
            return redirect('/transacao/aluguel') 
            
    except ValueError:
        # Erro: Número de dias inválido
        print("ERRO DE VALIDAÇÃO (Aluguel): Número de dias inválido.")
        return redirect('/transacao/aluguel')
        
    except Exception as e:
        print(f"ERRO EXCEPCIONAL (Aluguel): {e}") # Opcional: manter print para debug
        return redirect('/transacao/aluguel')


@route('/processar_devolucao_post', method='POST')
@checar_login
def processar_devolucao_post():
    """Rota para processar a devolução de um veículo."""
    placa = request.forms.get('placa')
    
    resultado = LOCADORA.processar_devolucao(placa)
        
    if "SUCESSO" in resultado:
            return redirect(f'/dashboard?msg={resultado}&status=success')
    else:
            return redirect(f'/dashboard?msg={resultado}&status=error')
            
    


# --- Rota para Servir Estáticos ---
@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root=STATIC_ROOT)


# --- Execução da Aplicação ---

if __name__ == '__main__':
    print(f"\nServidor Bottle iniciado em http://localhost:8080/")
    run(host='localhost', port=8080, debug=True, reloader=True) 

app = default_app()