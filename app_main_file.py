from flask import Flask , render_template
from database import *

app = Flask(__name__)

create_database('Health_database.db')
#create_table('sleep_cycle','Person_ID INTEGER PRIMARY KEY, Gender TEXT , Age INTEGER,Occupation TEXT, Sleep_Duration DECIMAL, Quality_of_Sleep INTEGER, Physical_Activity_level INTEGER, Stress_Level INTEGER, BMI_Category TEXT,Blood_Pressure INTEGER, Heart_Rate INTEGER, Daily_Steps INTEGER, Sleep_Disorder TEXT')
create_table()
data_from_csv('sleep_cycle', 'Sleep_health_and_lifestyle_dataset.csv')

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


