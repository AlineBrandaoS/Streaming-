from flask import Flask, render_template, request, redirect
from app.routes.cadastro import cadastro_route
from app.routes.home import home_route
from app.database.database import init_db
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

templates_dir = os.path.join(base_dir, 'app', 'templates')
static_dir = os.path.join(base_dir, 'app', 'static')

app = Flask(__name__, static_folder='app/static')


""" app.secret_key = "your_secret_key" #provisoria

#Configurações SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]

 """
# Database model





# Routes

app.register_blueprint(cadastro_route)
app.register_blueprint(home_route)



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    