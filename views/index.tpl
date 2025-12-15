<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - {{nome_locadora}}</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            background-color: #f4f7f6;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        header {
            background-color: #007bff;
            color: white;
            padding: 15px 30px;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            box-sizing: border-box;
        }
        header h1 {
            margin: 0;
            font-size: 1.5em;
        }
        .container {
            padding: 40px;
            width: 90%;
            max-width: 800px;
            text-align: center;
        }
        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .menu-item {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            text-decoration: none;
            color: #333;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .menu-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }
        .menu-item h3 {
            margin-top: 0;
            color: #007bff;
        }
        .menu-item p {
            font-size: 0.9em;
            color: #666;
        }
        .logout-link {
            color: white;
            text-decoration: none;
            padding: 8px 15px;
            border: 1px solid white;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .logout-link:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        .message-box {
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 4px;
            font-weight: bold;
            width: 100%;
            box-sizing: border-box;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
    </style>
</head>
<body>

    <header>
        <h1>{{nome_locadora}} - Menu Principal</h1>
        <a href="/logout" class="logout-link">Sair</a>
    </header>

    <div class="container">
        
        {% if mensagem %}
            <div class="message-box {{status}}">
                {{mensagem}}
            </div>
        {% endif %}
        
        <h2>Selecione uma Operação</h2>

        <div class="menu-grid">
            
            <a href="/cadastro/cliente" class="menu-item">
                <h3>Cadastrar Cliente 👤</h3>
                <p>Adiciona um novo cliente ao sistema da locadora.</p>
            </a>

            <a href="/cadastro/veiculo" class="menu-item">
                <h3>Cadastrar Veículo 🚗</h3>
                <p>Inclui um novo veículo na frota para aluguel.</p>
            </a>

            <a href="/transacao/aluguel" class="menu-item">
                <h3>Processar Aluguel 🔑</h3>
                <p>Realiza a transação de aluguel de um veículo disponível.</p>
            </a>

            <a href="/transacao/devolucao" class="menu-item">
                <h3>Processar Devolução ↩️</h3>
                <p>Finaliza o aluguel e calcula o valor a pagar.</p>
            </a>
            
        </div>
    </div>
    
</body>
</html>