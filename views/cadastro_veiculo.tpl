<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Veículo - {{nome_locadora}}</title>
    <style>
        /* Reutilizando CSS base */
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
        .main-content {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            width: 90%;
            max-width: 450px;
            margin-top: 40px;
            text-align: left;
        }
        h2 {
            color: #0056b3;
            margin-top: 0;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        form label {
            display: block;
            margin-top: 15px;
            margin-bottom: 5px;
            font-weight: bold;
            color: #555;
        }
        form input[type="text"],
        form input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        form button {
            background-color: #28a745;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 30px;
            font-size: 1em;
            transition: background-color 0.3s;
        }
        form button:hover {
            background-color: #1e7e34;
        }
        .back-link {
            display: block;
            margin-top: 20px;
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
        }
        .logout-link {
            color: white;
            text-decoration: none;
            padding: 8px 15px;
            border: 1px solid white;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <header>
        <h1>{{nome_locadora}}</h1>
        <a href="/logout" class="logout-link">Sair</a>
    </header>

    <div class="main-content">
        <h2>Cadastro de Novo Veículo</h2>
        
        <form method="POST" action="/cadastrar_veiculo_post">
            
            <label for="placa_veiculo">Placa (Ex: ABC1234):</label>
            <input type="text" id="placa_veiculo" name="placa" required>
            
            <label for="valor_diaria">Valor da Diária (R$):</label>
            <input type="number" id="valor_diaria" name="valor_diaria" step="0.01" min="0.01" required>
            
            <button type="submit">Cadastrar Veículo</button>
        </form>
        
        <a href="/dashboard" class="back-link">← Voltar ao Menu Principal</a>
    </div>
</body>
</html>