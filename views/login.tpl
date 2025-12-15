<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Locadora Queiroz</title>
    <style>
        /* CSS Integrado */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e9ebee; /* Fundo mais claro e suave */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15); /* Sombra mais destacada */
            width: 100%;
            max-width: 380px;
            text-align: center;
        }
        h2 {
            color: #0056b3; /* Azul escuro da marca */
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
            box-sizing: border-box; /* Garante que padding não afete a largura total */
            transition: border-color 0.3s;
        }
        .input-group input:focus {
            border-color: #007bff; /* Azul primário ao focar */
            outline: none;
        }
        .submit-button {
            width: 100%;
            background-color: #007bff;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1em;
            transition: background-color 0.3s ease;
        }
        .submit-button:hover {
            background-color: #0056b3;
        }
        .error-message {
            color: #d9534f; /* Vermelho para mensagens de erro */
            margin-top: 15px;
            padding: 10px;
            border: 1px solid #f2dede;
            background-color: #fcf2f2;
            border-radius: 5px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

    <div class="login-box">
        <h2>Acesso Administrativo</h2>

        {% if error %}
            <p class="error-message" id="errorMessage">{{ error }}</p>
        {% endif %}
        
        <form method="POST" action="/login" id="loginForm">
            <div class="input-group">
                <label for="username">Usuário</label>
                <input type="text" id="username" name="username" required>
            </div>

            <div class="input-group">
                <label for="senha">Senha</label>
                <input type="password" id="senha" name="senha" required>
            </div>

            <button type="submit" class="submit-button">
                Entrar
            </button>
        </form>
        
        <p style="margin-top: 25px; color: #777;">Usuário de teste: **admin / 123**</p>
        
        <p style="margin-top: 20px; font-size: 0.9em;">
            Não tem uma conta? <a href="/cadastrar" style="color: #007bff; text-decoration: none; font-weight: bold;">Crie uma aqui</a>.
        </p>
    </div>

    <script>
        // JavaScript Integrado (Validação básica de cliente e feedback de botão)
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('loginForm');
            const submitButton = form.querySelector('.submit-button');
            const usernameInput = document.getElementById('username');
            const senhaInput = document.getElementById('senha');

            form.addEventListener('submit', function(event) {
                // Aqui você pode adicionar validações extras antes do envio:
                if (usernameInput.value.trim() === "" || senhaInput.value.trim() === "") {
                    // Prevenção básica caso os campos não sejam preenchidos (além do 'required')
                    alert("Por favor, preencha todos os campos.");
                    event.preventDefault();
                    return;
                }
                
                // Feedback visual ao clicar no botão:
                submitButton.textContent = "Verificando...";
                submitButton.disabled = true;
            });
            
            // Lógica para remover a mensagem de erro após um tempo (melhor UX)
            const errorMessage = document.getElementById('errorMessage');
            if (errorMessage) {
                setTimeout(() => {
                    errorMessage.style.display = 'none';
                }, 5000); // 5 segundos
            }
        });
    </script>

</body>
</html>