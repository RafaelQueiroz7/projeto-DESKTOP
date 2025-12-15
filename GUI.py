import tkinter as tk
from tkinter import ttk, messagebox 
from package.locadora_app import Locadora 
from package.seguranca_app import GerenciadorUsuario

class LocadoraApp(tk.Tk):
    """Classe principal da aplicação GUI Tkinter."""
    
    def __init__(self):
        super().__init__()
        self.title("Locadora Queiroz - Sistema Administrativo")
        self.geometry("600x400") 
        self.resizable(False, False)
        
        self.LOCADORA = Locadora()
        self.USUARIOS = GerenciadorUsuario()
        
        self._criar_janela_login()

    # ====================================================================
    # 1. LÓGICA DE LOGIN
    # ====================================================================

    def _criar_janela_login(self):
        """Cria e exibe os widgets para a tela de login."""
        self.login_frame = ttk.Frame(self, padding="30 30 30 30")
        self.login_frame.pack(expand=True, fill='both')

        ttk.Label(self.login_frame, text="Acesso ao Sistema", font=('Arial', 18, 'bold')).pack(pady=20)

        ttk.Label(self.login_frame, text="Usuário:").pack(pady=5, anchor='w')
        self.username_entry = ttk.Entry(self.login_frame, width=30)
        self.username_entry.pack(pady=5)

        ttk.Label(self.login_frame, text="Senha:").pack(pady=5, anchor='w')
        self.password_entry = ttk.Entry(self.login_frame, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Botão de Login
        ttk.Button(self.login_frame, text="Entrar", command=self._processar_login).pack(pady=20)
        
        # Botão de Cadastro (NOVO)
        ttk.Button(self.login_frame, text="Criar Novo Usuário", 
                   command=self._criar_janela_cadastro_usuario).pack(pady=5)

        ttk.Label(self.login_frame, text="Usuário de teste: admin / 123", font=('Arial', 10)).pack(pady=10)


    def _processar_login(self):
        """Lógica de autenticação."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.USUARIOS.autenticar_usuario(username, password):
            messagebox.showinfo("Sucesso", f"Bem-vindo(a) à {self.LOCADORA.get_nome()}!")
            self.login_frame.destroy() 
            self._criar_dashboard()    
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")

    # ====================================================================
    # 2. LÓGICA DE CADASTRO DE USUÁRIO (NOVA)
    # ====================================================================
    
    def _criar_janela_cadastro_usuario(self):
        """Cria uma nova janela para o cadastro de usuário."""
        
        cadastro_window = tk.Toplevel(self) 
        cadastro_window.title("Criar Novo Usuário")
        cadastro_window.geometry("350x250")
        cadastro_window.grab_set() 
        
        form_frame = ttk.Frame(cadastro_window, padding="15")
        form_frame.pack(expand=True, fill='both')
        
        ttk.Label(form_frame, text="Nome de Usuário:", font=('Arial', 11)).pack(pady=5, anchor='w')
        username_entry = ttk.Entry(form_frame, width=30)
        username_entry.pack(pady=5)
        
        ttk.Label(form_frame, text="Senha:", font=('Arial', 11)).pack(pady=5, anchor='w')
        password_entry = ttk.Entry(form_frame, show="*", width=30)
        password_entry.pack(pady=5)
        
        ttk.Button(form_frame, text="Criar Conta", 
                   command=lambda: self._processar_cadastro_usuario(
                       username_entry.get(), 
                       password_entry.get(),
                       cadastro_window) 
                   ).pack(pady=20)

    def _processar_cadastro_usuario(self, username, password, janela):
        """Chama a lógica POO para cadastrar um novo usuário."""
        
        if not username or not password:
             messagebox.showerror("Erro de Entrada", "Usuário e senha são obrigatórios.")
             return
        
        # Chama o método da classe GerenciadorUsuario (que salva em usuarios_data.json)
        if self.USUARIOS.cadastrar_usuario(username, password):
            messagebox.showinfo("Sucesso", f"Usuário '{username}' criado com sucesso!")
            janela.destroy()
        else:
            messagebox.showerror("Erro", f"Nome de usuário '{username}' já existe.")

    # ====================================================================
    # 3. DASHBOARD (MENU PRINCIPAL) & RECARGA
    # ====================================================================
    
    def _recarregar_dashboard(self):
        """Destrói e recria o dashboard para refletir o estado atualizado (após transação)."""
        if hasattr(self, 'dashboard_frame'):
            self.dashboard_frame.destroy()
        self._criar_dashboard()


    def _criar_dashboard(self):
        """Cria e exibe a interface principal da Locadora com o menu de botões."""
        
        # Assume que o login_frame foi destruído
        self.dashboard_frame = ttk.Frame(self, padding="20")
        self.dashboard_frame.pack(expand=True, fill='both')
        
        ttk.Label(self.dashboard_frame, text=f"{self.LOCADORA.get_nome()} - Menu Principal", 
                  font=('Arial', 20, 'bold')).pack(pady=20)
        
        botoes_frame = ttk.Frame(self.dashboard_frame)
        botoes_frame.pack(pady=10)
        
        # 1. Cadastro Cliente
        ttk.Button(botoes_frame, text="1. Cadastrar Cliente", width=25,
                   command=self._criar_formulario_cliente).grid(row=0, column=0, padx=10, pady=10)
               
        # 2. Cadastro Veículo
        ttk.Button(botoes_frame, text="2. Cadastrar Veículo", width=25,
                   command=self._criar_formulario_veiculo).grid(row=0, column=1, padx=10, pady=10)

        # 3. Aluguel de Veículo
        ttk.Button(botoes_frame, text="3. Alugar Veículo", width=25,
                   command=self._criar_formulario_aluguel).grid(row=1, column=0, padx=10, pady=10)

        # 4. Devolução de Veículo
        ttk.Button(botoes_frame, text="4. Processar Devolução", width=25,
                   command=self._criar_formulario_devolucao).grid(row=1, column=1, padx=10, pady=10)
        
        ttk.Button(self.dashboard_frame, text="Sair do Sistema", command=self.quit).pack(pady=30)


    # ====================================================================
    # 4. OPERAÇÃO: CADASTRO DE CLIENTE
    # ====================================================================

    def _criar_formulario_cliente(self):
        """Cria uma nova janela (Toplevel) para o cadastro de clientes."""
        
        cliente_window = tk.Toplevel(self) 
        cliente_window.title("Cadastrar Novo Cliente")
        cliente_window.geometry("350x250")
        cliente_window.grab_set() 
        
        form_frame = ttk.Frame(cliente_window, padding="15")
        form_frame.pack(expand=True, fill='both')
        
        ttk.Label(form_frame, text="Nome Completo:").pack(pady=5, anchor='w')
        nome_entry = ttk.Entry(form_frame, width=30)
        nome_entry.pack(pady=5)
        
        ttk.Label(form_frame, text="CPF:").pack(pady=5, anchor='w')
        cpf_entry = ttk.Entry(form_frame, width=30)
        cpf_entry.pack(pady=5)
        
        ttk.Button(form_frame, text="Cadastrar", 
                   command=lambda: self._processar_cadastro_cliente(
                       nome_entry.get(), 
                       cpf_entry.get(),
                       cliente_window) 
                   ).pack(pady=20)

    def _processar_cadastro_cliente(self, nome, cpf, janela):
        """Chama a lógica POO e exibe o resultado."""
        
        if not nome or not cpf:
             messagebox.showerror("Erro de Entrada", "Nome e CPF são obrigatórios.")
             return

        resultado = self.LOCADORA.cadastrar_cliente(cpf, nome)
        
        if "SUCESSO" in resultado.upper():
            messagebox.showinfo("Cadastro OK", resultado)
            janela.destroy()
        else:
            messagebox.showerror("Erro de Cadastro", resultado)

    # ====================================================================
    # 5. OPERAÇÃO: CADASTRO DE VEÍCULO
    # ====================================================================
    
    def _criar_formulario_veiculo(self):
        """Cria uma nova janela (Toplevel) para o cadastro de veículos."""
        
        veiculo_window = tk.Toplevel(self) 
        veiculo_window.title("Cadastrar Novo Veículo")
        veiculo_window.geometry("350x280")
        veiculo_window.grab_set()
        
        form_frame = ttk.Frame(veiculo_window, padding="15")
        form_frame.pack(expand=True, fill='both')
        
        ttk.Label(form_frame, text="Placa (Ex: ABC1234):").pack(pady=5, anchor='w')
        placa_entry = ttk.Entry(form_frame, width=30)
        placa_entry.pack(pady=5)
        
        ttk.Label(form_frame, text="Valor da Diária (R$):").pack(pady=5, anchor='w')
        valor_diaria_var = tk.StringVar()
        valor_diaria_entry = ttk.Entry(form_frame, textvariable=valor_diaria_var, width=30)
        valor_diaria_entry.pack(pady=5)
        
        ttk.Button(form_frame, text="Cadastrar", 
                   command=lambda: self._processar_cadastro_veiculo(
                       placa_entry.get(), 
                       valor_diaria_var.get(), 
                       veiculo_window) 
                   ).pack(pady=20)

    def _processar_cadastro_veiculo(self, placa, valor_diaria_str, janela):
        """Chama a lógica POO e exibe o resultado para o cadastro de veículo."""
        
        if not placa or not valor_diaria_str:
             messagebox.showerror("Erro de Entrada", "Placa e Valor da Diária são obrigatórios.")
             return
             
        try:
            valor_diaria = float(valor_diaria_str)
            
            resultado = self.LOCADORA.cadastrar_veiculo(placa, valor_diaria)
            
            if "SUCESSO" in resultado.upper():
                messagebox.showinfo("Cadastro OK", resultado)
                janela.destroy()
            else:
                messagebox.showerror("Erro de Cadastro", resultado)
                
        except ValueError:
            messagebox.showerror("Erro de Entrada", "O Valor da Diária deve ser um número válido (ex: 150.50).")
        except Exception as e:
            messagebox.showerror("Erro Desconhecido", f"Ocorreu um erro: {e}")

    # ====================================================================
    # 6. OPERAÇÃO: ALUGUEL DE VEÍCULO
    # ====================================================================

    def _criar_formulario_aluguel(self):
        """Cria a janela para processar o aluguel."""
        
        clientes_obj = self.LOCADORA.get_clientes_list()
        veiculos_obj = self.LOCADORA.get_veiculos_disponiveis_list()
        
        clientes_opcoes = [f"{c.get_nome()} (CPF: {c.get_cpf()})" for c in clientes_obj]
        veiculos_opcoes = [f"{v.get_placa()} (R$ {'%.2f' % v.get_valorDiaria()})" for v in veiculos_obj]
        
        self.cliente_map = {op: c.get_cpf() for op, c in zip(clientes_opcoes, clientes_obj)}
        self.veiculo_map = {op: v.get_placa() for op, v in zip(veiculos_opcoes, veiculos_obj)}
        
        if not clientes_opcoes or not veiculos_opcoes:
            messagebox.showwarning("Aviso", "Não há clientes cadastrados ou veículos disponíveis.")
            return

        aluguel_window = tk.Toplevel(self) 
        aluguel_window.title("Processar Novo Aluguel")
        aluguel_window.geometry("400x350")
        aluguel_window.grab_set()
        
        form_frame = ttk.Frame(aluguel_window, padding="15")
        form_frame.pack(expand=True, fill='both')

        # 1. Combobox de Clientes
        ttk.Label(form_frame, text="Cliente:").pack(pady=5, anchor='w')
        self.cliente_combo = ttk.Combobox(form_frame, values=clientes_opcoes, state='readonly', width=30)
        self.cliente_combo.pack(pady=5)
        self.cliente_combo.set(clientes_opcoes[0])
        
        # 2. Combobox de Veículos
        ttk.Label(form_frame, text="Veículo Disponível:").pack(pady=5, anchor='w')
        self.veiculo_combo = ttk.Combobox(form_frame, values=veiculos_opcoes, state='readonly', width=30)
        self.veiculo_combo.pack(pady=5)
        self.veiculo_combo.set(veiculos_opcoes[0])
        
        # 3. Campo Dias
        ttk.Label(form_frame, text="Dias Previstos de Aluguel:").pack(pady=5, anchor='w')
        dias_entry = ttk.Entry(form_frame, width=30)
        dias_entry.pack(pady=5)
        
        # 4. Botão de Aluguel
        ttk.Button(form_frame, text="Processar Aluguel", 
                   command=lambda: self._processar_aluguel(
                       dias_entry.get(),
                       aluguel_window)
                   ).pack(pady=20)

    def _processar_aluguel(self, dias_str, janela):
        """Chama a lógica POO para alugar um veículo."""
        
        try:
            # Mapeamento do valor exibido para o CPF/Placa real
            cpf = self.cliente_map[self.cliente_combo.get()]
            placa = self.veiculo_map[self.veiculo_combo.get()]
            dias = int(dias_str)
            
            if dias <= 0:
                raise ValueError("Dias devem ser um número positivo.")

            resultado = self.LOCADORA.processar_aluguel(cpf, placa, dias)
            
            if "SUCESSO" in resultado.upper():
                messagebox.showinfo("Aluguel OK", resultado)
                janela.destroy()
                self._recarregar_dashboard()
            else:
                messagebox.showerror("Erro de Aluguel", resultado)
                
        except ValueError as ve:
            messagebox.showerror("Erro de Entrada", f"Entrada inválida. Dias deve ser um número inteiro positivo.")
        except KeyError:
            messagebox.showerror("Erro de Seleção", "Por favor, selecione um Cliente e um Veículo.")
        except Exception as e:
            messagebox.showerror("Erro Desconhecido", f"Ocorreu um erro: {e}")

    # ====================================================================
    # 7. OPERAÇÃO: DEVOLUÇÃO DE VEÍCULO
    # ====================================================================

    def _criar_formulario_devolucao(self):
        """Cria a janela para processar a devolução."""
        
        placas_alugadas = self.LOCADORA.consultar_frota_alugada()
        
        if not placas_alugadas:
            messagebox.showwarning("Aviso", "Não há veículos em aluguel para devolver.")
            return

        devolucao_window = tk.Toplevel(self) 
        devolucao_window.title("Processar Devolução")
        devolucao_window.geometry("350x200")
        devolucao_window.grab_set()
        
        form_frame = ttk.Frame(devolucao_window, padding="15")
        form_frame.pack(expand=True, fill='both')

        # 1. Combobox de Veículos Alugados
        ttk.Label(form_frame, text="Placa do Veículo a devolver:").pack(pady=5, anchor='w')
        self.devolucao_combo = ttk.Combobox(form_frame, values=placas_alugadas, state='readonly', width=30)
        self.devolucao_combo.pack(pady=5)
        self.devolucao_combo.set(placas_alugadas[0])
        
        # 2. Botão de Devolução
        ttk.Button(form_frame, text="Confirmar Devolução", 
                   command=lambda: self._processar_devolucao(
                       self.devolucao_combo.get(),
                       devolucao_window)
                   ).pack(pady=20)


    def _processar_devolucao(self, placa, janela):
        """Chama a lógica POO para processar a devolução."""
        
        try:
            resultado = self.LOCADORA.processar_devolucao(placa)
            
            if "SUCESSO" in resultado.upper():
                messagebox.showinfo("Devolução OK", resultado)
                janela.destroy()
                self._recarregar_dashboard()
            else:
                messagebox.showerror("Erro de Devolução", resultado)
                
        except Exception as e:
            messagebox.showerror("Erro Desconhecido", f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    # Garante que o usuário admin exista para o primeiro login
    USUARIOS_SETUP = GerenciadorUsuario()
    USUARIOS_SETUP.cadastrar_usuario("admin", "123")
    
    app = LocadoraApp()
    app.mainloop()