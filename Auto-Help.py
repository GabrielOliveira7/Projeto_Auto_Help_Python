from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Rota principal - Página de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para processar o formulário de login
@app.route('/login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']

    # Conecte-se ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Verifique as credenciais do usuário no banco de dados
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    # Verifique se um usuário foi encontrado
    if user:
        # Autenticação bem-sucedida, redirecione para a página principal
        return redirect('/home')
    else:
        # Credenciais inválidas, redirecione para a página de login novamente
        return redirect('/')

# Rota para a página principal após o login
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

