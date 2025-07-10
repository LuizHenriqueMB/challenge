from flask import Flask, request, render_template_string

app = Flask(__name__)

# Fake AWS Secrets - para gitleaks e bandit detectarem
AWS_ACCESS_KEY = "AKIAFAKEACCESSKEY1234"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAKEKEY"

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        user = request.form.get("username")
        message = f"Bem-vindo, {user}!"  # XSS refletido aqui

    # render_template_string é perigoso!
    return render_template_string("""
        <h2>Login</h2>
        <form method="post">
            <input name="username" placeholder="Usuário">
            <input name="password" type="password" placeholder="Senha">
            <button type="submit">Entrar</button>
        </form>
        <p>{{ message }}</p>
    """, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
