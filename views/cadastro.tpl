<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro - Locadora Queiroz</title>
    <style>
        /* Reutiliza o CSS do login para manter a consistência visual */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e9ebee;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            width: 100%;
            max-width: 380px;
            text-align: center;
        }
        h2 {
            color: #0056b3;
            margin-bottom: 30px;
            font-size: 1.8em;
        }
        .input-group {
            margin-bottom: 20px;
            text-align: left;
        }
        .input-group label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: bold;
        }
        .input-group input {
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            transition: border-color 0.3s;
        }
        .input-group input:focus {
            border-color: #007bff;
            outline: none;
        }
        .submit-button {
            width: 100%;
            background-color: #28a745; /* Cor verde para cadastro */
            color: white;
            padding: 12px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1em;
            transition: background-color 0.3s ease;
        }
        .submit-button:hover {
            background-color: #1e7e34;
        }
        .error-message {
            color: #d9534f;
            margin-top: 15px;
            padding: 10px;
            border: 1px solid #f2dede;
            background-color: #fcf2f2;
            border-radius: 5px;
            font-size: 0.9em;
        }
        .success-message {
            color: #28a745;
            margin-top: 15px;
            padding: 10px;
            border: 1px solid #d4edda;
            background-color: #e9f7eb;
            border-radius: 5px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

    <div class="login-box">
        <h2>Criar Conta</h2>

        {% if error %}
            <p class="error-message">{{ error }}</p>
        {% endif %}

        {% if success %}
            <p class="success-message">Conta criada com sucesso! Faça login abaixo.</p>
        {% endif %}
        
        <form method="POST" action="/cadastrar" id="cadastroForm">
            <div class="input-group">
                <label for="username">Novo Usuário</label>
                <input type="text" id="username" name="username" required>
            </div>

            <div class="input-group">
                <label for="senha">Nova Senha</label>
                <input type="password" id="senha" name="senha" required>
            </div>

            <button type="submit" class="submit-button">
                Criar Conta
            </button>
        </form>
        
        <p style="margin-top: 20px; font-size: 0.9em;">
            <a href="/login" style="color: #007bff; text-decoration: none;">Voltar para o Login</a>
        </p>
    </div>

</body>
</html>