from flask import Flask,Blueprint ,render_template, request, redirect, url_for
from ..database.database import get_db_connection
import sqlite3

cadastro_route = Blueprint('cadastro', __name__, template_folder='../templates')

# rota inicial
@cadastro_route.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
# nova rota
@cadastro_route.route('/form-cadastro', methods=['POST'])
def cadastrar():
    # acesso aos dados do formulario
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    try:
        conn = get_db_connection()
        conn.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?,?,?)",(nome, email, senha))
        
        conn.commit()
        conn.close()
        
    except sqlite3.IntegrityError:
        return "Erro: E-mail já cadastrado!", 409
    
    return redirect(url_for('home.html'))
# rota que os dados foram adicionados ao banco de dados com sucesso
@cadastro_route.route('/success')
def success():
    return "<h1>Cadastro realizado com sucesso</h1>"