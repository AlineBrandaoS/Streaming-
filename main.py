from flask import Flask, render_template, request, redirect
from app.routes.cliente import cliente_route
from app.database.database import init_db
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)
app.secret_key = "your_secret_key" #provisoria

#Configurações SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]


# Database model





# Routes

app.register_blueprint(cliente_route)



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    