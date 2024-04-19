from flask import Flask , render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/data')
def display_data():
    
    conn = sqlite3.connect('Health_database.db')
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


