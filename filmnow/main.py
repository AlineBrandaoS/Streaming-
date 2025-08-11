from flask import Flask
from app.routes.cliente import cliente_route
from app.database.database import init_db
import sqlite3
app = Flask (__name__)

app.register_blueprint(cliente_route)



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
   