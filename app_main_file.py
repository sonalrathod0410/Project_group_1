from flask import Flask , render_template
import sqlite3
from pathlib import Path
import os

base_path = Path().cwd()
db_name = "Health_database.db"
db_path = base_path / db_name
my_path= os.path.join(os.path.dirname(__file__), db_name)
print(my_path)
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/data')
def display_data():
    
    conn = sqlite3.connect(my_path)
    cursor = conn.cursor()   
    cursor.execute("SELECT * FROM sleep_cycle LIMIT 15")
    data = cursor.fetchall()   
    conn.close()

    return render_template('data.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


