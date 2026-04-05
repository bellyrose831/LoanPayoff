#source: https://ttsmp3.com/
#source: https://render.com/docs/deploy-flask
#source: https://dashboard.render.com/web/srv-d6uu461aae7s73f7qmog/deploys/dep-d6uu46haae7s73f7qn10
#deployment link: https://dashboard.render.com/

#pip install flask
#run using "python app.py"
# pip install psycopg2

from flask import Flask, render_template
from db import get_db_connection
import os

app = Flask(__name__)

@app.route('/')
def main():
    conn = get_db_connection()
    
    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE testTable (
        brand VARCHAR(255),
        model VARCHAR(255),
        year INT
        );"""
    )
    cur.execute("""
        INSERT INTO testTable (brand, model, year)
        VALUES
        ('kia', 'forte', 2022),
        ('camaro', 'camerillo', 2000)"""
    )
    cur.execute('SELECT * from testTable')
    results = cur.fetchall()
    cur.execute('drop table testTable')
    cur.close()
    return render_template('home.html', test=results)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)