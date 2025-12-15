<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Locadora Queiroz</title>
    <style>
        /* CSS Integrado (Estilização da Página) */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            text-align: center;
        }
        .container {
            background: white;
            padding: 40px 60px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
            font-size: 2.5em;
        }
        .login-button {
            background-color: #007bff; /* Cor primária azul */
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1em;
            transition: background-color 0.3s ease;
            text-decoration: none; /* Garante que pareça um botão */
            display: inline-block;
        }
        .login-button:hover {
            background-color: #0056b3; /* Azul mais escuro no hover */
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Bem-vindo à Locadora Queiroz</h1>
        <p>Seu destino para aluguel de veículos de qualidade.</p>
        
        <button id="loginButton" class="login-button">
            Fazer Login
        </button>
    </div>

    <script>
        // JavaScript Integrado (Lógica de Redirecionamento)
        document.addEventListener('DOMContentLoaded', function() {
            const loginButton = document.getElementById('loginButton');
            
            // Adiciona um listener de evento ao clique do botão
            loginButton.addEventListener('click', function() {
                // Redireciona o usuário para a rota de login (/login)
                window.location.href = '/login';
            });
        });
    </script>

</body>
</html>