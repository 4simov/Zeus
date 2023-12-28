from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration de la base de données SQLite
DATABASE = 'users.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('inscription.html')

@app.route('/inscription', methods=['POST'])
def inscription():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Vérification du mot de passe
    if password != confirm_password:
        return "Les mots de passe ne correspondent pas."

    # Hash du mot de passe avant de le stocker
    hashed_password = generate_password_hash(password, method='sha256')

    # Insertion dans la base de données
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)