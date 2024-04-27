from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventario'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products')
    data = cur.fetchall()
    return render_template('index.html', products = data)

@app.route('/addProduct', methods=['POST'])
def addProduct():
    if request.method == 'POST':
        fullname = request.form['fullname']
        value = request.form['value']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO products (nombre, valor) VALUES (%s, %s)', (fullname, value))
        mysql.connection.commit()
        flash('Producto agregado!')

        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def getProduct(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('editProduct.html', product = data[0])

@app.route('/update/<id>', methods = ['POST'])
def updateProduct(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        value = request.form['value']
        cur= mysql.connection.cursor()
        cur.execute("""
            UPDATE products
            SET nombre = %s,
                valor = %s
            WHERE id = %s
        """, (fullname, value, id))
        mysql.connection.commit()
        flash('Producto actualizado!')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def deleteProduct(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM products WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Producto eliminado!')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)