from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventario'
mysql = MySQL(app)

@app.route('/')
def Index():
    return 'PRUEBA'

@app.route('/addProduct')
def addProduct():
    return 'AGREGAR PRODUCTO'

@app.route('/editProduct')
def editProduct():
    return 'EDITAR PRODUCTO'

@app.route('/deleteProduct')
def deleteProduct():
    return 'ELIMINAR PRODUCTO'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)