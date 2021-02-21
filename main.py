# coding: utf-8
# Serveur Python

# 1 - on importe les librairies dont on a besoin
# flask est le framework web
from flask import Flask, render_template
# sqlite pour faire du sqlite :)
import sqlite3

database_path = "data/sql_manga.db"

# 2 - on instancie notre app flask
app = Flask('app', template_folder='views')

# 3 - on définit les pages

# .. sur la page d'accueil


@app.route('/')
def home_page():
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    results = cursor.execute(
        "SELECT * FROM Mangas LIMIT 100")

    return render_template('index.html', all_Mangas=results)

# .. sur l'url d'un film


@app.route('/Mangas/<Manga_id>')
def Mangas_page(Manga_id):
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    # en réalité cette approche est dangereuse (-> injections SQL)
    # mais dans un souci de simplicité on le garde comme ça :)
    result = cursor.execute("SELECT * FROM Mangas WHERE id = " + Manga_id)

    result = result.fetchone()

    return render_template('movie.html', Mangas=result)


# 4 - on lance notre serveur web
app.run(host='localhost', port=3000, debug=True)
